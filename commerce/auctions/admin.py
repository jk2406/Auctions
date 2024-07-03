from django.contrib import admin
from .models import bid,bid_comments,list_auction
# Register your models here.
admin.site.register(bid)
admin.site.register(bid_comments)
admin.site.register(list_auction)
