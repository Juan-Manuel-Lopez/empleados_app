from django.contrib import admin
from empleados_app.models import Empleados, UserProfileInfo, User

# Register your models here.
admin.site.register(Empleados)
admin.site.register(UserProfileInfo)
