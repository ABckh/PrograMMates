# Generated by Django 4.0.4 on 2022-05-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0010_alter_users_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, default='default/avatardefault_92824.png', null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
