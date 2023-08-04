from django.db import models
from users.models import User
from carts.models import Cart
from enum import Enum

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [(tag, tag.value) for tag in OrderStatus]

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=choices, 
                              default=OrderStatus.CREATED)
    shiping_total = models.DecimalField(default=5 , max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0 , max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart)