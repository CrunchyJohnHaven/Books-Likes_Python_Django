# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Belt', '0006_auto_20180126_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='belt',
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.AddField(
            model_name='review',
            name='book_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='Belt.Book'),
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Belt.Belt'),
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(),
        ),
    ]
