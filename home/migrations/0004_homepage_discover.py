# Generated by Django 3.1 on 2020-09-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200903_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='discover',
            field=models.CharField(default='Be one of the first to discover this unique learning experience', max_length=128),
        ),
    ]
