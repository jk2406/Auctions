# Generated by Django 5.0.6 on 2024-07-03 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_description_bid_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='Contact_ID',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='Number_of_buyers_before',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='full_Description',
        ),
    ]