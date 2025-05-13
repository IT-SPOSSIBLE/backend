from django.db import models

from api.models import UserTB
from conversation.models import Conversation
class Message(models.Model):
    id=models.AutoField(primary_key=True)
    conversation=models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name='conversation_messages')
    sender_id=models.ForeignKey(UserTB,on_delete=models.CASCADE,related_name='message_sender')
    message_description=models.CharField(max_length=None)
    sent_at=models.DateTimeField()


    def message_create(id,conversation,sender_id,message_description,sent_at):
        message=Message.objects.create(id=id,conversation=conversation,sender_id=sender_id,message_description=message_description,sent_at=sent_at)
        return message
