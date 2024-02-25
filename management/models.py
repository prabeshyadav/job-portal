from django.db import models

from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email =models.EmailField(unique=True)
    is_recruiter= models.BooleanField(default=False)
    is_applicant=models.BooleanField(default=False)
    has_resume=models.BooleanField(default=False)

