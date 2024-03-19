from django.urls import path
from . import views
urlpatterns = [
    path('', views.YourView, name='YourView'),
]