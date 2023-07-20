from django.db import models
import uuid
from login.models import User
# Create your models here.
class HistoryAction(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list_selected_products = models.TextField(null = True)
    list_selected_categories = models.TextField(null = True)
    list_selected_sales = models.TextField(null = True)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='history_logs')