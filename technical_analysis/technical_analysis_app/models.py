from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
    
    
class BaseCandle(models.Model):
    timestamp = models.DateTimeField()
    open = models.DecimalField(max_digits=20, decimal_places=8)
    high = models.DecimalField(max_digits=20, decimal_places=8)
    low = models.DecimalField(max_digits=20, decimal_places=8)
    close = models.DecimalField(max_digits=20, decimal_places=8)
    volume = models.DecimalField(max_digits=20, decimal_places=8)

    class Meta:
        abstract = True  # So Django won't create this table


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"