from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    credit=models.PositiveIntegerField(default=0)
    due=models.PositiveIntegerField(default=0)
    phone=models.PositiveIntegerField()
    product=models.CharField(max_length=200,default='')
    date=models.DateField(auto_now_add=True)
    
    
     
    

    def __str__(self):
        return self.name

