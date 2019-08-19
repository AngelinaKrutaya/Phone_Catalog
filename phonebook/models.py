from django.db import models

class Contact(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateField(auto_now=True)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.Name)+' '+str(self.RegDate)
# Create your models here.
