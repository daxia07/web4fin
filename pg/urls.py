from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe, name='recipe'),
    path('test/', views.test, name='test')
]
