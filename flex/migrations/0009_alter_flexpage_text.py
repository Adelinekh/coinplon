# Generated by Django 4.1.2 on 2022-10-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0008_alter_flexpage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='text',
            field=models.TextField(blank=True, default='Amet sed quisquam sit aliquam tempora ut. Dolorem eius est adipisci adipisci numquam. Adipisci porro quaerat dolor tempora etincidunt est. Sit ipsum numquam consectetur ut. Modi neque porro etincidunt.', max_length=500, null=True),
        ),
    ]
