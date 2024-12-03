import os
import uuid


from django.db import models

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
    Warden = models.ForeignKey(Warden, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Warden.FirstName} {self.GunModel}"

    class Meta:
        db_table = 'armoury'


# python3 manage.py makemigrations
# python3 manage.py migrate
# python manage.py populate
