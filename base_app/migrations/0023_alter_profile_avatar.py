# Generated by Django 4.2.4 on 2023-11-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0022_appointments_time_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='images/'),
        ),
    ]