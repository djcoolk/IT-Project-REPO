# Generated by Django 5.0.9 on 2024-10-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role_id',
            new_name='role',
        ),
    ]
