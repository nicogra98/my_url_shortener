import uuid
from django.db import models

# Create your models here.

class UrlModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)