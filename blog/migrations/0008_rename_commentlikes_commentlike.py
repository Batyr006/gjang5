# Generated by Django 4.2.9 on 2024-03-14 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commentlikes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentLikes',
            new_name='CommentLike',
        ),
    ]
