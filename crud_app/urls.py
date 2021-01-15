from django.urls import path
from . import views
urlpatterns = [
    path('',views.BmiView.as_view(), name='index'),
    #path('form',views.form, name='form')
]
