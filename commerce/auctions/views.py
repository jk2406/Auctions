from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import BidForm
from .models import User,bid,list_auction,bid_tracker,bid_comments
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from . import util
import markdown2
bids = bid.objects.all()
user_name =None
GlUser = None

def index(request):
    return render(request,'auctions/index.html', {'bids':bids,'bid_user':GlUser})
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            global user_name
            user_name=username
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
@login_required
def bid_create(request):
    if request.method == 'POST':
        form = BidForm(request.POST,request.FILES)
        if form.is_valid():
            new_bid = form.save(commit=False)  # Create an instance but don't save to the database yet
            new_bid.username = request.user.username  # Set the username to the logged-in user's username
            new_bid.UID = util.random_id_generator() 
            BidTracker = bid_tracker()
            BidTracker.UID = new_bid.UID
            BidTracker.allBids = new_bid.starting_bid
            BidTracker.save()
            new_bid.save()
            return redirect('index') 
        else:
            context={'form':form}
            return render(request,'auctions/makebid.html',context)
    context = {'form':BidForm()}
    return render(request,'auctions/makebid.html',context)
def addtowatch(request):
    if request.method == 'POST':
        ID = request.POST["addwatchlist"]
        try:
            watchlist = bid.objects.get(UID=ID)
            ListAuction = list_auction()
            ListAuction.UID = watchlist.UID
            y =  request.user.username
            item =  list_auction.objects.filter(username_watch =y)
            if  item.filter(UID=ListAuction.UID).exists():
                error = "ID already in watchlist"
                
                return render(request,'auctions/index.html',{"error":error,"bids":bids})
            ListAuction.username_watch = request.user.username
            ListAuction.Username= watchlist.username
            ListAuction.Title=watchlist.title
            ListAuction.Description=watchlist.short_description
            ListAuction.Starting_bid=watchlist.starting_bid
            ListAuction.Image=watchlist.image
            ListAuction.save()
            success = "Item successfully added to watchlist"
            return render(request,'auctions/index.html',{"bids":bids,"success":success})
        except  ObjectDoesNotExist:
            
            error_in_watchlist_addition = f"ID {ID} doesn't exist"
            return render(request,'auctions/index.html',{"error":error_in_watchlist_addition,"bids":bids})
@login_required
def watchlist(request):
    list_auction.username_watch = request.user.username
    userName =list_auction.username_watch
    watchList = list_auction.objects.filter(username_watch = userName)
    return render(request,'auctions/watchlist.html',{'watchlist':watchList})
def removewatch(request):       
        if request.method == 'POST':
            ID = request.POST["removewatchlist"]
            try:
                watchlist = list_auction.objects.filter(UID=ID)
                watchlist.delete()
                return redirect('watchlist')    
            except ObjectDoesNotExist:
                error = "ID doesn't exist"
                return render(request,'auctions/watchlist.html',{"error":error})
def BidOn(request):
    if request.method == 'POST':
        bid_id= request.POST["bid_id"]
        username = request.user.username
        try:
            old_bid = bid.objects.get(UID=bid_id)
        except ObjectDoesNotExist:
            error = "ID doesn't exist"
            return render(request,"auctions/index.html",{"error":error,"bids":bids})
        new_bid_amount = int(request.POST["bid_bid"])
        if old_bid.username== username:
            error="You can't bid on your own Bid"
            return render(request,'auctions/BidOn.html',{"bids":bids,"error":error})
        if new_bid_amount>=old_bid.starting_bid:
            old_bid.starting_bid = new_bid_amount
            old_bid.save()
            
            Tracker = bid_tracker()
            Tracker.bidder = username
            global GlUser
            GlUser= username
            Tracker.UID = bid_id
            Tracker.Bid_amount=new_bid_amount
            Tracker.save()
            success = "Bid placed successfully"
            return render(request,'auctions/index.html',{"bids":bids,"bid_user":username,"success":success})
        else:
            error = "New bid amount must be greater than or equal to previous one"
            return render(request,'auctions/BidOn.html',{"bids":bids,"error":error})    
    return render(request,'auctions/BidOn.html',{"bids":bids},)
def specific_user_bids(request):
    if request.method == 'POST':
        closing_bid_id = request.POST["closing_bid_id"]
        item = bid.objects.filter(UID=closing_bid_id)
        item.delete()
        success = "Bid successfully closed"
        userName = request.user.username
        user_specific_bids = bid.objects.filter(username =userName )
        return render(request,'auctions/specificBid.html',{"bids":user_specific_bids,"success":success})
    userName = request.user.username
    user_specific_bids = bid.objects.filter(username =userName )
    return render(request,'auctions/specificBid.html',{"bids":user_specific_bids,"bid_user":GlUser})   
def get_entry(request,ID):
    item = bid.objects.filter(UID=ID)
    all_comments = bid_comments.objects.filter(UID=ID)
    item = bid.objects.filter(UID=ID)
    return render(request,'auctions/full_info.html',{"bids":item,"comments":all_comments})
def make_comments(request):
    if request.method =='POST':
       comment= markdown2.markdown(request.POST["comments_bids"])
       GlUID = request.POST["comment_of_particular"]
       COMMENT= bid_comments()
       COMMENT.UID = GlUID
       COMMENT.username = request.user.username
       COMMENT.comment = comment
       COMMENT.save()
       all_comments = bid_comments.objects.filter(UID=GlUID)
       item = bid.objects.filter(UID=GlUID)
       return render(request,'auctions/full_info.html',{"comments":all_comments,"bids":item})
    return render(request,'auctions/comment.html',{})