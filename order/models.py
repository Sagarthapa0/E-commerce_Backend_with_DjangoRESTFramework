from django.db import models
from user.models import User
from products.models import Product

# Create your models here.


class Order(models.Model):
    product=models.ManyToManyField(Product)
    total=models.FloatField(blank=False,null=False)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    is_ordered=models.BooleanField(default=False)
    date_ordered=models.DateTimeField(auto_now_add=True)
    is_delivered=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"Order #{self.id} {self.buyer.username}"
    

    
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255,default="nepal")
    status = models.CharField(max_length=100, choices=[("Pending", "Pending"), ("Shipped", "Shipped"), ("Delivered", "Delivered")],null=True)

    def __str__(self) -> str:
        return f"{self.order} "
    

    


