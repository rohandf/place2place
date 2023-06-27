from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class order(models.Model):
    order_id = models.ForeignKey(User)