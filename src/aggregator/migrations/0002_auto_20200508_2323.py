# Generated by Django 3.0.6 on 2020-05-08 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0001_auto_20200506_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasource',
            options={'ordering': ('last_use_time',), 'verbose_name': 'Источник', 'verbose_name_plural': 'Источники'},
        ),
    ]
