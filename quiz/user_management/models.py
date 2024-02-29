import uuid

from django.db import models


# Create your models here.

class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=255, null=False)
    user_email = models.EmailField(unique=True, null=False)
    user_address = models.TextField(null=True)
    user_role = models.CharField(max_length=29, null=False)

