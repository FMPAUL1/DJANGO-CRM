from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    zipcode=models.IntegerField()
    
    def __str__(self):
        return (f"{self.lastname} {self.firstname}" )