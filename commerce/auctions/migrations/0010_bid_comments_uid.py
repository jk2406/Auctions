# Generated by Django 5.0.6 on 2024-07-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_allbids_bid_tracker_bid_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid_comments',
            name='UID',
            field=models.TextField(default='DE000'),
        ),
    ]
