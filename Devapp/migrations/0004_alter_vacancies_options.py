# Generated by Django 4.0.6 on 2022-08-10 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0003_alter_events_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]