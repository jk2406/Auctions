# Generated by Django 5.0.6 on 2024-07-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_bid_comments_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid_tracker',
            old_name='UID',
            new_name='Unique',
        ),
    ]
