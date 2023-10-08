# Generated by Django 4.2.4 on 2023-09-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='specialties',
        ),
        migrations.AddField(
            model_name='lawyer',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='areasOfExpertise',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='city',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='lisenceStatus',
            field=models.CharField(choices=[('active', 'active'), ('suspended', 'suspended'), ('revoked', 'revoked')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='yearsOfExperience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='averageRating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='hourlyRate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]