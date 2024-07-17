from django.db import models

# Create your models here.
class Machines(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=300)
    initiated_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title  
