# Generated by Django 3.1.7 on 2021-04-05 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jb_main', '0009_auto_20210404_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='last_tweeted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
