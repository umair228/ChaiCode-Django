from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE= [
        ('ML', 'Milk Chai'),
        ('BL', 'Black Chai'),
        ('GR', 'Green Chai'),
        ('WH', 'White Chai'),
        ('OT', 'Other Chai'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    currency = models.CharField(max_length=3,default='PKR')
    description = models.TextField(default='empty')
    image = models.ImageField(upload_to='chai/images')
    offer = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE,default='OT')

    def __str__(self):
        return self.name