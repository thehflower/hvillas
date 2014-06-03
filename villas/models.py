from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

#model Villa 
class Villa(models.Model):
    name = models.CharField(max_length=10)
    feet = models.CharField(max_length=5,
        validators=[
            RegexValidator(
                r'^[0-9]+$',                 #only digits are allowed
                'Only 0-9 are allowed.',
                'Invalid Number'
            )])
    def __str__(self):  # Python 3: 
        return self.name

class Resident(models.Model):
    email=models.EmailField(max_length=50)
    name= models.CharField(max_length=50)
    villa=models.OneToOneField(Villa, primary_key=True)
