# Generated by Django 4.1.7 on 2023-03-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_user',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
    ]