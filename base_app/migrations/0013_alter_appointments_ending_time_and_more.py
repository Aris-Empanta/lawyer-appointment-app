# Generated by Django 4.2.4 on 2023-10-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0012_alter_availablehours_lawyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='ending_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='availablehours',
            name='ending_time',
            field=models.DateTimeField(null=True),
        ),
    ]