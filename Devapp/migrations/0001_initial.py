# Generated by Django 4.0.6 on 2022-08-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('salary', models.TextField()),
                ('type_of', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]