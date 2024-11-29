
# Create your models here.
from django.db import models
from django.utils.timezone import now



class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=50, unique=True)
    order_date = models.DateTimeField(default=now)
    total_amount_of_order = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.customer_name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=now)
    total_amount_of_order = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.customer.customer_name
    
