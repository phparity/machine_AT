from django.db import models
import random
import string



your_key = (''.join(random.choices(string.ascii_lowercase, k=15)))

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    key = models.CharField(unique=True, max_length=100, blank=True,help_text="If you not Enter Key It Take Autometicaly")

    
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=15))
        super().save(*args, **kwargs)
        
        
class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    IP = models.CharField(max_length=100)
    port = models.CharField(max_length=10)
    
    
class Employee(models.Model):
    employee_id = models.IntegerField()
    name =  models.CharField(max_length=100)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)  
    employee_uid = models.CharField(default=None, max_length=15)
    password = models.IntegerField()
    card_no = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
   
class NewEmployee(models.Model):
        
    name =  models.CharField(max_length=100)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)  
    employee_uid = models.CharField(default=None, max_length=15)
    password = models.IntegerField()
    card_no = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
     
    
class Attandance(models.Model):
    employee_id_id = models.IntegerField()
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    Date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    Date_Time = models.CharField(max_length=500)
    
    