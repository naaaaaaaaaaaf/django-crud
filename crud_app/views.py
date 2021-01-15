from django.shortcuts import render
from django.views.generic import ListView
from .forms import BmiForm
from .models import Bmi
# Create your views here.
class BmiView(ListView):
    template_name = 'bmi/all.html'
    model = Bmi

# 関数ベースだとこんな感じになる
def all_bmi(request):
    params = {
        'data': Bmi.objects.all()
    }
    return render(request,'bmi/all.html',params)