# Generated by Django 2.1.5 on 2019-04-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remiljscrumy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumprojectrole',
            name='role',
            field=models.CharField(max_length=20),
        ),
    ]
