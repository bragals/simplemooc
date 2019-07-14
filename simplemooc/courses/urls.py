from django.contrib import admin
from django.urls import include, path
from simplemooc.courses import views
app_name='courses'

urlpatterns = [
    path('cursos/', views.index, name='index'),
   
]
