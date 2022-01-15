from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
    register_number = models.CharField(max_length=20)
    register_date = models.DateField()
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    another_name = models.CharField(max_length=100)
    nid = models.IntegerField()
    employee_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name


class OfficialInfo(models.Model):
    official_register_number = models.CharField(max_length=20)
    official_register_date = models.DateField()

    def __str__(self):
        return self.official_register_number


class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    another_fullname = models.CharField(max_length=100)
    national_id = models.IntegerField()
    employee_avatar = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.full_name

