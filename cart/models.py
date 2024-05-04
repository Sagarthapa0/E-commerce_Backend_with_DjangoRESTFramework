from django.db import models
from products.models import Product
from user.models import User

# Create your models here.
class Cart(models.Model):
    product=models.ManyToManyField(Product)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,default=1)

    def __str__(self) -> str:
        return self.products