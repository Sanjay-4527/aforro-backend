
from django.db import models
from apps.stores.models import Store
from apps.products.models import Product

class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requested = models.IntegerField()
