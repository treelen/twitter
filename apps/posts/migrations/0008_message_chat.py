# Generated by Django 4.1.5 on 2023-02-22 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_likecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, verbose_name='Сообщение')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитан')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_chat', to=settings.AUTH_USER_MODEL, verbose_name='ID чата')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_from_user', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение от пользователя')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_to_user', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение к пользователю')),
            ],
            options={
                'verbose_name': ('Сообщение в чате',),
                'verbose_name_plural': 'Сообщение в чатах',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='Чат пользователя')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='Чат к пользователя')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
    ]