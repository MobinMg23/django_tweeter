# Generated by Django 5.1.3 on 2024-11-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='hashtag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]