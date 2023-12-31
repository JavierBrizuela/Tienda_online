from django.db import models
from users.models import User
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reference = models.CharField(max_length=300, blank=True)
    postal_code = models.CharField(max_length=10)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postal_code
    
    @property
    def address(self):
        return f'{self.city}-{self.state}-{self.country}'