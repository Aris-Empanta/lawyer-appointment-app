# Generated by Django 4.2.4 on 2023-11-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0021_remove_appointments_client_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='time_booked',
            field=models.DateTimeField(null=True),
        ),
    ]
