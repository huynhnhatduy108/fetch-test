from django.db import models
from models.brand.models import Brand

# Create your models here.
class Car(models.Model):
    id = models.BigAutoField(db_column="id",primary_key=True) 
    name = models.CharField(db_column='name', blank=True, null=True, max_length=255)
    color = models.CharField(db_column='color', blank=True, max_length=255)
    logo = models.CharField(db_column='logo', blank=True, null=True, max_length=255)
    description = models.TextField(db_column='description', blank=True, null=True)
    brand =  models.ForeignKey(Brand, db_column='brand_id', on_delete=models.PROTECT, blank=True, null=True, related_name="brand_name")

    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True, blank=True, null=True)
    deleted_flag = models.IntegerField(db_column='deleted_flag', blank=True, null=True, default=0)

    def __str__(self):
        return str(self.id)