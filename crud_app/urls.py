from django.urls import path
from . import views
urlpatterns = [
    path('',views.BmiView.as_view(), name='index'),
        
    path('create',views.CreateBmi.as_view(), name='create'),

    #path('form',views.form, name='form')
]
