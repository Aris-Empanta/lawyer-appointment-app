# Generated by Django 4.2.4 on 2023-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0014_alter_availablehours_lawyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/profile-pics/avatar.jpg', null=True, upload_to=''),
        ),
    ]
