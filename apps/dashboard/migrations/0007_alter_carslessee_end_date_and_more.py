# Generated by Django 4.1.7 on 2023-04-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_carslessee_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carslessee',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='carslessee',
            name='start_date',
            field=models.DateField(),
        ),
    ]