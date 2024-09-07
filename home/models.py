from django.db import models

# Create your models here.
class ContactForm(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "  {}   {}  {}  {}  ".format(self.Name, self.Email,self.Message,self.created_at)


class RegisterForm(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Username=models.CharField(max_length=25)
    Password=models.CharField(max_length=25)

    def __str__(self):
        return "  {}   {}  {}  {}  ".format(self.Name, self.Email,self.Username,self.Password)

class ImageForm(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/')