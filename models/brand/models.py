from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.BigAutoField(db_column="id",primary_key=True) 
    name = models.CharField(db_column='name', blank=True, null=True, max_length=255)

    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True, blank=True, null=True)
    deleted_flag = models.IntegerField(db_column='deleted_flag', blank=True, null=True, default=0)

    def __str__(self):
        return str(self.id)