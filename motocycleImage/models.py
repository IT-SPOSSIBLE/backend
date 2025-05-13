from django.db import models




class MotocycleImage(models.Model):
    id=models.AutoField(primary_key=True)
    moto=models.ForeignKey('product.Product',on_delete=models.CASCADE,related_name='product_image')
    imageUrl=models.URLField(max_length=200,blank=False)
    is_primary=models.BooleanField(default=False)
    uploaded_at=models.DateTimeField()


    def create_gallery(id,moto,imageUrl,is_primary,uploaded_at):
        motocycleImage=MotocycleImage.objects.create(id=id,moto=moto,imageUrl=imageUrl,is_primary=is_primary,uploaded_at=uploaded_at)
        return motocycleImage

    
