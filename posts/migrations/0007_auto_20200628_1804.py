# Generated by Django 3.0.3 on 2020-06-28 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200626_2252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modified',)},
        ),
    ]