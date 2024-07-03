from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class bid(models.Model):
    username = models.CharField(max_length=100,default='default_username')
    title = models.CharField(max_length=100)
    starting_bid = models.IntegerField(default=0)
    short_description = models.CharField(max_length=9999999)
    image = models.ImageField(upload_to='images/',null=True)
    UID = models.TextField(default='DE000')
    full_Description = models.CharField(max_length=999999999,default='default description')
    Number_of_buyers_before = models.IntegerField(default=0)
    Contact_ID = models.EmailField(default='example@dummy.com')
class bid_comments(models.Model):
    UID = models.TextField(default='DE000')
    username=models.TextField(default='Nothing')
    comment = models.CharField(max_length=9999999999)
class list_auction(models.Model):
    username_watch = models.CharField(max_length=100,default='default_username')
    Username = models.CharField(max_length=100,default='default')
    Title = models.CharField(max_length=100,default='default')
    Starting_bid = models.IntegerField(default=0)
    Description =models.CharField(max_length=9999999,default='default')
    Image = models.ImageField(upload_to='images_watchlist/',null=True)
    UID = models.TextField(default='DE000')
class bid_tracker(models.Model):
    UID = models.TextField(default='DE000')
    bidder = models.TextField(max_length=100,default="dummy")
    Bid_amount = models.IntegerField(default=0)