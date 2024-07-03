from django import forms
from django.db import models
from .models import bid,bid_comments
class BidForm(forms.ModelForm):
    class Meta:
       model = bid
       fields = ('title', 'short_description', 'image', 'starting_bid','full_Description','Contact_ID','Number_of_buyers_before')
       widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
            'full_description': forms.Textarea(attrs={'cols': 80, 'rows': 20},)
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
class BidComments(forms.ModelForm):
    model=bid_comments
    fields =('comment')
    widgets={
        'comment':forms.Textarea(attrs={'cols': 80, 'rows': 20})
    }
