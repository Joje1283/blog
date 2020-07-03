from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
# from .forms import PostForm
from .models import Post, Contact# , Tag


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
