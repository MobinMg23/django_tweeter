# Generated by Django 5.1.3 on 2024-12-06 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0007_remove_comment_likes_alter_like_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='django_app.tweet'),
        ),
    ]
