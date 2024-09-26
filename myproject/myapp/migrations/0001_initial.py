# Generated by Django 5.0.9 on 2024-09-25 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('role_id', models.CharField(max_length=3)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('password_hash', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=50)),
                ('profile_picture', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_verified', models.CharField(max_length=1)),
            ],
        ),
    ]
