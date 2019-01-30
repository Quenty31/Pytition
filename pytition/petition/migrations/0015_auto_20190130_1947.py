# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-30 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0014_auto_20181205_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petitiontemplate',
            name='confirmation_email_sender',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='newsletter_subscribe_mail_from',
            field=models.EmailField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='newsletter_subscribe_mail_to',
            field=models.EmailField(blank=True, max_length=500),
        ),
    ]
