# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'first_player_win'), ('C', 'second_player_win'), ('D', 'Draw')], default='A', max_length=1)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_first_player', to=settings.AUTH_USER_MODEL)),
                ('next_to_move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_to_move', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(max_length=300)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tictactoe.Game')),
            ],
        ),
    ]
