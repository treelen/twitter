# Generated by Django 4.1.5 on 2023-02-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='post_poster/'),
        ),
    ]
