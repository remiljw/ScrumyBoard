# Generated by Django 2.2 on 2019-04-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remiljscrumy', '0007_auto_20190415_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1)),
                ('role', models.IntegerField(default=6)),
                ('profile_img', models.TextField(default='https://res.cloudinary.com/louiseyoma/image/upload/v1546701687/profile_pic.png')),
                ('pwd_reset_token', models.CharField(default='000011112222', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unsubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remiljscrumy.CustomUser')),
            ],
        ),
    ]