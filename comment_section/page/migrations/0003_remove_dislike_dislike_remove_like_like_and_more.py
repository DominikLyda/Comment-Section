# Generated by Django 4.0.4 on 2022-06-05 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0002_comments_podcast_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislike',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AddField(
            model_name='dislike',
            name='comment',
            field=models.ForeignKey(default=420, on_delete=django.db.models.deletion.CASCADE, to='page.comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(default=420, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(default=420, on_delete=django.db.models.deletion.CASCADE, to='page.comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=420, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
