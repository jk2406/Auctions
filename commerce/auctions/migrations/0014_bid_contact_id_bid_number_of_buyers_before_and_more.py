# Generated by Django 5.0.6 on 2024-07-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_bid_contact_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='Contact_ID',
            field=models.EmailField(default='example@dummy.com', max_length=254),
        ),
        migrations.AddField(
            model_name='bid',
            name='Number_of_buyers_before',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bid',
            name='full_Description',
            field=models.CharField(default='default description', max_length=999999999),
        ),
    ]
