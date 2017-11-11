# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=30)),
                ('body_text', models.CharField(max_length=100)),
                ('put_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('n_comment', models.IntegerField()),
                ('n_pingback', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('author', models.ManyToManyField(to='user.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Blog')),
            ],
        ),
    ]