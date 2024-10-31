# Generated by Django 5.1.1 on 2024-10-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0006_alter_botuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='user_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
