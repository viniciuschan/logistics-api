# Generated by Django 2.1.8 on 2019-04-22 00:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_remove_logisticsnet_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticsnet',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='logisticsnet',
            name='path_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(verbose_name='path_data'),
        ),
    ]
