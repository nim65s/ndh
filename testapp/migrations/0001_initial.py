# Generated by Django 2.0 on 2017-12-06 02:35

from django.db import migrations, models

import autoslug.fields
import ndh.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('year_in_school', models.IntegerField(choices=[(1, 'freshman'), (2, 'sophomore'), (3, 'junior'), (4, 'senior')], default=1)),
                ('tests', models.IntegerField(default=42)),
                ('moment', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(ndh.models.Links, models.Model),
        ),
    ]
