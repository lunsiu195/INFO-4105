# Generated by Django 4.2.7 on 2023-11-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledpage',
            name='availability',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='crawledpage',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
