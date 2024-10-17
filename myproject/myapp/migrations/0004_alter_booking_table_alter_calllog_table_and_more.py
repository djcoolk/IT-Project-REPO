# Generated by Django 5.0.9 on 2024-10-14 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_role_id_user_role'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booking',
            table='bookings',
        ),
        migrations.AlterModelTable(
            name='calllog',
            table='call_logs',
        ),
        migrations.AlterModelTable(
            name='chatbotlog',
            table='chatbot_logs',
        ),
        migrations.AlterModelTable(
            name='chatlog',
            table='chat_logs',
        ),
        migrations.AlterModelTable(
            name='counselloravailability',
            table='counsellor_availabilities',
        ),
        migrations.AlterModelTable(
            name='counsellorprofile',
            table='counsellor_profiles',
        ),
        migrations.AlterModelTable(
            name='moodtracking',
            table='mood_tracking',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notifications',
        ),
        migrations.AlterModelTable(
            name='paymenthistory',
            table='payment_history',
        ),
        migrations.AlterModelTable(
            name='role',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='session',
            table='sessions',
        ),
        migrations.AlterModelTable(
            name='subscriptionplan',
            table='subscription_plans',
        ),
        migrations.AlterModelTable(
            name='usersubscription',
            table='user_subscriptions',
        ),
    ]
