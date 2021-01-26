from django.db import models

# Create your models here.
class user_reg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=15)
class items(models.Model): 
    item_name=models.CharField(max_length=50)
    item_q=models.CharField(max_length=50)
    uid=models.ForeignKey(user_reg,on_delete=models.CASCADE)
    status=models.IntegerField(max_length=1)
    gdate=models.DateField()