# Generated by Django 3.0.5 on 2020-05-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source_datetime', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('language', models.CharField(blank=True, max_length=15, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=180, unique=True)),
                ('hash', models.CharField(db_index=True, editable=False, max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-timestamp'],
            },
        ),
    ]
