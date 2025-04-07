from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)  # Product title
    description = models.TextField()          # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Discount value
    stock = models.PositiveIntegerField()     # Number of items in stock
    #category = models.CharField(max_length=100)  # Product category
    created_at = models.DateTimeField(auto_now_add=True)  # Date the product was added
    updated_at = models.DateTimeField(auto_now=True)      # Last update time
    published_at = models.DateTimeField(blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', default='default.png', blank=True, null=True)

    def __str__(self):
        return self.title