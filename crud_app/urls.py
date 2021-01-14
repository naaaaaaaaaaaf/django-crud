from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_bmi, name='index'),
    path('form',views.form, name='form')
]
