import uuid

from django.db import models


# Create your models here.
class ProductCategoryModel(models.Model):
    cid = models.CharField(max_length=5, primary_key=True, default=str(
        uuid.uuid4().int)[:5], editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
