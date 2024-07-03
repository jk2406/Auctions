from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bidcreate",views.bid_create,name="bid_create"),
    path("addtowatch",views.addtowatch,name="add_to_watchlist"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("remwatch",views.removewatch,name="remove_from_watchlist"),
    path("bidOn",views.BidOn,name="bid_on"),
    path("user_bid",views.specific_user_bids,name="specific_bid"),
    path("<str:ID>",views.get_entry,name="get_entry"),
    
    path('make_comments/',views.make_comments,name='make_comments')
]
