import os
import uuid


from django.db import models
from django.db.migrations import swappable_dependency


# Create your models here.

def generate_unique_name(instance, filename):
    name = uuid.uuid4() #
    full_file_name = f'{name}-{filename}'
    return os.path.join("profile_pictures", full_file_name)


# Create your models here.
class Warden(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Age = models.PositiveSmallIntegerField(default=0)
    Gender = models.CharField(max_length=10)
    Weight = models.PositiveIntegerField(default=0)
    ServiceNumber = models.PositiveIntegerField(default=0)
    ProfilePicture = models.ImageField(upload_to=generate_unique_name, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} "

    class Meta:
        db_table = 'Wardens'


class Armoury(models.Model):
    GunModel = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    Warden = models.ForeignKey(Warden, constrained('wardens'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Warden.FirstName} {self.GunModel}"

    class Meta:
        db_table = 'armoury'

class Issuing(models.Model):
    Gun = models.OneToOneField(Armoury, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    expected_return_date = models.DateField()
    return_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Gun

    @property
    def fine_total(self):
        if self.return_date and self.expected_return_date and self.return_date > self.expected_return_date:
            amount = (self.return_date - self.expected_return_date).days * 13
            return amount
        return 0
    class Meta:
        db_table = 'issuing'
        verbose_name = 'Issuing'
        verbose_name_plural = 'Issuings'
        ordering = ('status', 'expected_return_date')



class Payment(models.Model):
    issuing = models.ForeignKey(Issuing, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=120)
    code = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# python3 manage.py makemigrations
# python3 manage.py migrate
# python manage.py populate
