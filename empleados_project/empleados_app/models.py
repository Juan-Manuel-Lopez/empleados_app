from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleados(models.Model):
    EMP_ID = models.IntegerField(unique=True)
    NOMBRE = models.CharField(max_length=25)
    AP_PATERNO = models.CharField(max_length=25)
    AP_MATERNO = models.CharField(max_length=25)
    TELEFONO = models.CharField(max_length=20)
    FECHA_INGRESO = models.DateField
    DEPARTAMENTO = models.CharField(max_length=264)
    SALARIO =models.IntegerField
    def __str__(self):
        return self.NOMBRE + ' '+ self.AP_PATERNO

# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='empleados_app/profile_pics',blank=True)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
