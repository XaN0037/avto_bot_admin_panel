# Generated by Django 4.1.7 on 2023-04-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_carslessee_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carslessee',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='carslessee',
            name='start_date',
        ),
    ]
