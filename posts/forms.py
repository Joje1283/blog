from django.forms import models
from django import forms
from .models import Post, Tag


class PostForm(models.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    tags = forms.CharField(required=False, max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.tag_set.all():
            self.fields['tags'].widget.attrs['value'] = ','.join(self.instance.tag_set.values_list('name', flat=True))

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.cleaned_data.get('tags'):
            tag_list = [tag.strip() for tag in self.cleaned_data.get('tags').split(',')]
            qs = []
            for tag in tag_list:
                if not Tag.objects.filter(name=tag):
                    q = Tag.objects.create(name=tag)
                    qs.append(q)
            old_save_m2m = self.save_m2m
            def save_m2m():
                old_save_m2m()
                for q in qs:
                    post.tag_set.add(q)
            self.save_m2m = save_m2m
        if commit:
            post.save()
            self.save_m2m()
        return post


