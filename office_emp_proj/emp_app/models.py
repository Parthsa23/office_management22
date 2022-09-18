from django.db import models


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90)
    dept = models.CharField(max_length=90, blank=True)
    salary = models.IntegerField(default=0)
    location = models.CharField(max_length=100, blank=True)
    bonus = models.IntegerField(default=0)
    role = models.CharField(max_length=90, blank=True)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s " % (self.first_name, self.last_name, self.role)
