# Generated by Django 3.2.7 on 2022-08-24 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0013_auto_20220819_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='Devapp.organization'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='Devapp.organization'),
        ),
        migrations.AlterField(
            model_name='video',
            name='organization1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Devapp.organization'),
        ),
    ]