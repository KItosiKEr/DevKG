# Generated by Django 3.2.7 on 2022-08-19 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0009_auto_20220819_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events1', to='Devapp.company'),
        ),
    ]