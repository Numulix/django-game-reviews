# Generated by Django 3.1.4 on 2020-12-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.URLField(default=None),
        ),
    ]
