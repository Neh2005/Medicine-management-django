from django.db import models
class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Typically passwords should be hashed

    def __str__(self):
        return self.email
