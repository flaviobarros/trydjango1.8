# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('signup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newsletter.SignUp')),
            ],
            bases=('newsletter.signup',),
        ),
    ]
