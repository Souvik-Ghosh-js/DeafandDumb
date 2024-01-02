from django.db import models

# Create your models here.
# models.py
from django.db import models

class Guardian(models.Model):
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    monthly_income = models.FloatField(default=0.0)

class Student(models.Model):
    name = models.CharField(max_length=255)
    father = models.ForeignKey(Guardian, on_delete=models.CASCADE, related_name='father')
    mother = models.ForeignKey(Guardian, on_delete=models.CASCADE, related_name='mother')
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, related_name='guardian')
    date_of_birth = models.DateField()
    address = models.TextField()

class AdmissionData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    residential_certificate = models.FileField(upload_to='doc/')
    adhaar_card = models.FileField(upload_to='doc/')
    weight_of_child = models.IntegerField(null= True)
    has_disability = models.BooleanField(default=False)
    disability_certificate = models.FileField(upload_to='doc/', blank=True, null=True)
    applied_for_disability_certificate = models.BooleanField(default=False)
    medical_report = models.FileField(upload_to='doc/')
    cast_certificate = models.FileField(upload_to='doc/',null=True)
    taking_medicines_daily = models.BooleanField(default=False)
    behaves_inappropriately = models.BooleanField(default=False)
    problem_description = models.TextField(blank=True, null=True)
    hears_name_when_called = models.BooleanField(default=False)
    received_allowance = models.BooleanField(default=False)
    enrollment_class = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)

class Query(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
