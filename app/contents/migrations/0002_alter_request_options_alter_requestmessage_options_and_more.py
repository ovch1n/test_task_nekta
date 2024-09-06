# Generated by Django 5.1.1 on 2024-09-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['-created_at'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='requestmessage',
            options={'ordering': ['-created_at'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='request',
            name='content',
            field=models.TextField(blank=True, max_length=2555, null=True, verbose_name='Текст'),
        ),
    ]
