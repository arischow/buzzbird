# Generated by Django 2.2.3 on 2019-07-02 13:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190702_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
