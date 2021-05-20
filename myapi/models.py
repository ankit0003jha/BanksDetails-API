from django.db import models

# Create your models here.

class Branches(models.Model):
    ifsc = models.CharField(primary_key=True ,max_length=20)
    bank_id = models.BigIntegerField(blank=True, null=True)
    branch = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:  
        db_table = "myapi_branches"

