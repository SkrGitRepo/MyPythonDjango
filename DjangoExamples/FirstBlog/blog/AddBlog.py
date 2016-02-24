'''
Created on Oct 30, 2015

@author: sumkuma2
'''
from django.conf import settings

if __name__ == '__main__':
    pass

settings.configure()
from blog.models import posts
from datetime import datetime



#saving records to Table 'posts'
datetimestamp = datetime.today()
addpost = posts(author='Zaheer',title='News',bodytext='Phone news',timestamp=datetimestamp)

addpost.save()