from django.db import models

#This BaseModel is for all the models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)