from django.db import models

# Create your models here.

class User(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    user_name     = models.CharField(max_length=50, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    password      = models.CharField(max_length=300)
    phone_number  = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
