from django.conf.urls import url
from django.urls import path
from empleados_app import views

app_name = 'emp_app'


urlpatterns = [
  path('',views.index,name='index'),
  #path('',views.user,name='users'),
  #path('alta/',views.empleado,name='emp')
  path('media/',views.empleado,name='media'),
  path('alta/',views.empleado,name='alta_emp'),
  path('register/',views.register,name='register'),
  path('user_login/',views.user_login,name='user_login'),
]
