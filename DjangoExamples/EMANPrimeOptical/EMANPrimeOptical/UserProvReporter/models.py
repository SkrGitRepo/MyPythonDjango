from django.db import models

# Create your models here.
class USER_TABLE(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    typeofuser = models.IntegerField()
    subtypeofuser = models.IntegerField()
    userdescription = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'user_table'