# Generated by Django 5.1.1 on 2024-10-31 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_alter_botuser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='user_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]