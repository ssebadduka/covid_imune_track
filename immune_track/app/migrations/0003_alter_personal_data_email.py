# Generated by Django 3.2 on 2021-04-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_personal_data_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_data',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
