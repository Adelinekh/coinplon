# Generated by Django 4.1.2 on 2022-10-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='subtitle',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
