from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(null=True,upload_to="images")

    def __str__(self):
        return self.name


class Reviews(models.Model):
    comment=models.CharField(max_length=120)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return self.comment
    
class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


# localhost:8000/products/1/
# get
# delete

# pip install djangorestframework
# localhost:8000/products/1/addtocart
# post
# 