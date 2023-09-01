# Generated by Django 4.2.4 on 2023-09-01 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialties', models.TextField()),
                ('description', models.TextField()),
                ('averageRating', models.IntegerField()),
                ('hourlyRate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='base_app.client')),
                ('lawyer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='base_app.lawyer')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLawyer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lawyer',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='base_app.profile'),
        ),
        migrations.AddField(
            model_name='client',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='base_app.profile'),
        ),
    ]