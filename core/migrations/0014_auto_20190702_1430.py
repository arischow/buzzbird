# Generated by Django 2.2.3 on 2019-07-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190702_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='link',
            field=models.URLField(db_index=True, null=True),
        ),
    ]