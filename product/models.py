from django.db import models

from category.models import Category
from motocycleImage.models import MotocycleImage
from api.models import UserTB


class Product(models.Model):
    PRODUCT_CHOICE_STATUS=[
        ("available","available"),
        ("sold","sold"),
    ]
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    price=models.FloatField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_of_product')
    motocycleImage=models.ForeignKey(MotocycleImage,on_delete=models.CASCADE,related_name='image_of_product')
    posted_by=models.ForeignKey(UserTB,on_delete=models.CASCADE,related_name='product_posted_by')
    created_at=models.DateTimeField()
    status=models.CharField(max_length=10,choices=PRODUCT_CHOICE_STATUS,default="available")


    def create_product(id,title,price,category,motocycleImage,posted_by,created_at,status):
        product=Product.objects.create(id=id,title=title,price=price,category_id=category,motocycleImage=motocycleImage,posted_by=posted_by,created_at=created_at,status=status)
        return product


