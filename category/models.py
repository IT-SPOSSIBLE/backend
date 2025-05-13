from django.db import models

from api.models import UserTB

class Category(models.Model):
    id=models.AutoField(),
    category_name=models.CharField(max_length=255)
    created_by=models.ForeignKey(UserTB,on_delete=models.CASCADE,related_name='category_created_by')
    created_at=models.DateTimeField()



    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def create_category(id,category_name,created_by,created_at):
        category=Category.objects.create(id=id,category_name=category_name,created_by=created_by,created_at=created_at)
        return category
