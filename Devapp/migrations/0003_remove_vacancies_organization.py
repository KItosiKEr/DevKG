# Generated by Django 3.2.7 on 2022-08-17 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0002_rename_vacancies_vacancies_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancies',
            name='organization',
        ),
    ]