# Generated by Django 4.1.5 on 2023-02-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='email',
            field=models.EmailField(max_length=25),
        ),
    ]