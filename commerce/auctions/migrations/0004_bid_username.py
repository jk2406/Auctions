# Generated by Django 5.0.6 on 2024-06-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_bid_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='username',
            field=models.CharField(default='default_username', max_length=100),
        ),
    ]