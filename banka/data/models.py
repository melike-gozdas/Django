from django.db import models
from django.urls import reverse
# Create your models here.
class Data(models.Model):
    CustomerId = models.IntegerField(primary_key=True, serialize=False, unique=True, auto_created=True)
    Surname = models.CharField(max_length=50, null=True)
    CreditScore = models.IntegerField(null=True)
    Geography = models.CharField(max_length=50, null=True)
    Gender = models.CharField(max_length=10, null=True)
    Age = models.IntegerField(null=True)
    Tenure = models.IntegerField(null=True)
    Balance = models.FloatField(null=True)
    NumOfProducts = models.IntegerField(null=True)
    HasCrCard = models.IntegerField(null=True)
    IsActiveMember = models.IntegerField(null=True)
    EstimatedSalary = models.FloatField(null=True)
    Exited = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.CustomerId

    def get_absolute_url(self):
        return reverse('data:detail', kwargs={'CustomerId': self.CustomerId})
        #return "/data/{}".format(self.CustomerId)
