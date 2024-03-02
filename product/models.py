from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key = True)
    p_name = models.CharField(max_length=50)
    p_qty = models.IntegerField()
    p_desc = models.CharField(max_length=200)
    p_price = models.IntegerField()
    poster = models.ImageField(upload_to='images/',null=True)
    category = models.ForeignKey(Category,related_name = 'category', null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.p_name
    