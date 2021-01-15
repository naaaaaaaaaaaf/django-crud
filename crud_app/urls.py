from django.urls import path
from . import views
urlpatterns = [
    path('',views.BmiView.as_view(), name='index'),
    path('detail/<int:pk>', views.BmiDetail.as_view(), name='detail'),
    path('create',views.CreateBmi.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateBmi.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteBmi.as_view(), name='delete')

    #path('form',views.form, name='form')
]
