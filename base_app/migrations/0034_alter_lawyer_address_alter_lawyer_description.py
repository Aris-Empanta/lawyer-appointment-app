# Generated by Django 4.2.4 on 2023-12-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0033_alter_lawyer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]