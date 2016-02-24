'''
Created on Oct 13, 2015

@author: sumkuma2
'''
from django.forms.models import ModelForm
from OrderApp.models import *

class ProductsForm(ModelForm):
    '''
    classdocs
    '''
    class Meta:
        model = Products
        fields = ['productCode','productName','productVendor','productDescription']
        #return fields


    def __init__(self, params):
        '''
        Constructor
        '''
        