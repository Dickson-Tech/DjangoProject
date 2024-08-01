from django.db import models

# Create your models here.
# models.py
class User(models.Model): #: This line defines a Django model named User. This class inherits from models.Model, indicating that it is a Django model. you need to write this before creating any model.
    username = models.CharField(max_length=20)
    fname = models.CharField(max_length=100)
    lname =models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    gender = models.CharField(max_length=10)
    dob =models.DateField()
    password1 =models.CharField(max_length=100)

    def __str__(self): # This method provides a human-readable representation of the User object. It's useful for debugging and for displaying information about the object. In this case, it returns a string containing the User's name and His/Her Personal details.
        return f"{self.username} - {self.lname}"
