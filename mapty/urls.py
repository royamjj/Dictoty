from django.urls import path
from .import views

app_name = 'mapty'

urlpatterns = [
    path('', views.index, name='index'),
]