# Generated by Django 4.0.4 on 2022-05-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0004_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(),
        ),
    ]
