# Generated by Django 4.2.4 on 2023-11-03 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0020_appointments_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='client_username',
        ),
        migrations.AddField(
            model_name='appointments',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.client'),
        ),
    ]
