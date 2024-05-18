from django.db import models

# Create your models here.

class ContractStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name
    
class Contract(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    status = models.ForeignKey(ContractStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
