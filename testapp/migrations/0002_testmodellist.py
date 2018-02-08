# Generated by Django 2.0.1 on 2018-02-08 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelList',
            fields=[
                ('testmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.TestModel')),
            ],
            options={
                'abstract': False,
            },
            bases=('testapp.testmodel',),
        ),
    ]
