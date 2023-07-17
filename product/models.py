from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default= 0.00)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title