# Generated by Django 5.1.1 on 2024-10-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0005_alter_botuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'ordering': ['-created_at'], 'verbose_name': 'BOT USER', 'verbose_name_plural': 'BOT USERS'},
        ),
    ]
