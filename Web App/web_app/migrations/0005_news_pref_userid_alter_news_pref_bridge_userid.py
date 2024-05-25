# Generated by Django 5.0.6 on 2024-05-15 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_mirror_mirror_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_pref',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='news_users', to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news_pref_bridge',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID'),
        ),
    ]
