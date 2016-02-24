from django import forms
'''
Created on Nov 1, 2015

@author: sumkuma2
'''
from .models import posts
from .models import users

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = posts
        #fields = ['author','title','bodytext']
        #exclude = ('timestamp',)
        fields = "__all__" 


class userSignupForm(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"