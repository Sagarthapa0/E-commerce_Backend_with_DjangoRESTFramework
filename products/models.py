from django.db import models
from user.models import User
from category.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    description=models.CharField(max_length=100,null=True,blank=True)
    price=models.FloatField(default=99)
    stock_quantity=models.IntegerField(default=1,null=True,blank=True)
    rating=models.IntegerField(default=4)
    image = models.ImageField(default='th.png')

    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None,null=True,blank=True)

    seller=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.comment
    
    class Meta:
        unique_together = ['product', 'user']  # Ensure each user can only review a product once

    def __str__(self):
        return f"Review for {self.product} by {self.user}"
