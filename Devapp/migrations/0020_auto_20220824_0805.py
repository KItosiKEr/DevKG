# Generated by Django 3.2.7 on 2022-08-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devapp', '0019_auto_20220824_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='upload_location'),
        ),
    ]