from django.db import models

from api.models import UserTB

from product.models import Product

class Conversation(models.Model):
    CONVERSATION_CHOICE=[
        ('read', 'read'),
        ('unread', 'unread')
    ]
    id=models.AutoField(primary_key=True)
    moto=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_conversation')
    buyer=models.ForeignKey(UserTB,on_delete=models.CASCADE,related_name='buyer_conversation')
    started_at=models.DateTimeField()
    status=models.CharField(max_length=10,choices=CONVERSATION_CHOICE,default="unread")


    def create_conversation(id,moto,buyer,started_at,status):
        conversation=Conversation.objects.create(id=id,moto=moto,buyer=buyer,started_at=started_at,status=status)
        return conversation