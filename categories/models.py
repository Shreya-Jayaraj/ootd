from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key = True)
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.cat_name)