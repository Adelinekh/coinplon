# Generated by Django 4.1.2 on 2022-10-12 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_subtitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexpage',
            old_name='subtitle',
            new_name='texte',
        ),
    ]