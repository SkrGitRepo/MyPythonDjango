'''
Created on Apr 2, 2016

@author: sumkuma2
'''
from rest_framework import serializers
from models import USER_TABLE

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_TABLE
        field = ('userid','username','subtypeofuser')