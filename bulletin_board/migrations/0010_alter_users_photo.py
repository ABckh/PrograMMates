# Generated by Django 4.0.4 on 2022-05-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0009_alter_advert_title_alter_users_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, default='~/home/abehod_y/avatardefault_92824.png', null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
