from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

#one to many
class ChaiReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE,related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.chai.name} reviewed by {self.user.username}'


## many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity,related_name='stores')

    def __str__(self):
        return self.name


## one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'{self.chai.name} certificate'