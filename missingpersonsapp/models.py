from django.db import models

# Create your models here.
class Missing(models.Model):
    Date_Missing = models.DateField(default=0)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField(default=0)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    
    def __str__(self):
        return(self.First_Name + " " + self.Last_Name)