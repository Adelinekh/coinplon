# Generated by Django 4.1.2 on 2022-10-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_alter_flexpage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(blank=True, default='Ipsum eius dolore neque dolorem. Eius eius dolor quiquia consectetur. Ipsum dolore eius quisquam dolorem. Porro quisquam non quiquia sit ipsum magnam. Etincidunt etincidunt sed consectetur modi etincidunt voluptatem. Voluptatem adipisci quaerat quiquia etincidunt ut. Magnam dolor aliquam quiquia ipsum dolor.', max_length=500, null=True),
        ),
    ]
