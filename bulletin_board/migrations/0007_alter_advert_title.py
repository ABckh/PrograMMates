# Generated by Django 4.0.4 on 2022-05-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0006_alter_advert_title_alter_users_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(choices=[('', 'Not selected'), ('JavaScript', 'JavaScript'), ('HTML and CSS', 'HTML and CSS'), ('Python', 'Python'), ('C++', 'C++'), ('TypeScript', 'TypeScript'), ('Rust', 'Rust'), ('Java', 'Java'), ('Scheme', 'Scheme'), ('Kotlin', 'Kotlin'), ('C#', 'C#'), ('Perl', 'Perl'), ('PHP', 'PHP'), ('Scala', 'Scala'), ('Swift', 'Swift'), ('SQL', 'SQL'), ('Golang (GO)', 'Golang (GO)'), ('Ruby', 'Ruby'), ('C', 'C'), ('Visual Basic .NET', 'Visual Basic .NET'), ('Delphi', 'Delphi')], max_length=80),
        ),
    ]
