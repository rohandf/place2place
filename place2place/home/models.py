from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class order(models.Model):
    order = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ordr')
    order_number = models.AutoField(primary_key=True)
    cargo_type = models.CharField(max_length=100)
    cargo_weight = models.DecimalField(decimal_places=2,max_digits=7)
    delivery_time = models.IntegerField()
    cargo_destination = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=12)
    date_of_order = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2,max_digits=20,blank=True,null=True)
        
    def __str__(self):
        return self.cargo_type
    
    class Meta:
        ordering=('-date_of_order',)