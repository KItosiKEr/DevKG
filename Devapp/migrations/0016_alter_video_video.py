# Generated by Django 3.2.7 on 2022-08-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0015_auto_20220824_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='upload_location'),
        ),
    ]