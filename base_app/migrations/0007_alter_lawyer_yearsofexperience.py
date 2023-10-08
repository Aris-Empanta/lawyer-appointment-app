# Generated by Django 4.2.4 on 2023-10-01 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_alter_lawyer_yearsofexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='yearsOfExperience',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)]),
        ),
    ]