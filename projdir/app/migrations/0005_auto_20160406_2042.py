# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160406_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codehubcreateeventmodel',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='codehubeventquestionmodel',
            name='question_text',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='codehubtopiccommentmodel',
            name='comment_text',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='codehubtopicmodel',
            name='topic_detail',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user_description',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
