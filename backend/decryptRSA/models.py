from django.db import models
import uuid

class DeviceClient(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    private_key = models.CharField(max_length=200 , null = True)
    public_key = models.CharField(max_length=200 , null = True)
    created=models.DateTimeField()
    date_activate = models.DateTimeField(null = True)
    expired = models.IntegerField()
    
    def __str__(self):
        return str(self.id)