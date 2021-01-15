from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Bmi
from django.urls import reverse_lazy
# Create your views here.
class BmiView(ListView):
    template_name = 'bmi/all.html'
    model = Bmi

class BmiDetail(DetailView):
    template_name = 'bmi/detail.html'
    model = Bmi

class CreateBmi(CreateView):
    template_name = 'bmi/create.html'
    model = Bmi
    fields = ('name', 'bmi')
    success_url = reverse_lazy('index')
class UpdateBmi(UpdateView):
    template_name = 'bmi/create.html'
    model = Bmi
    fields = ('name','bmi')
    success_url = reverse_lazy('index')
# 関数ベースだとこんな感じになる
def all_bmi(request):
    params = {
        'data': Bmi.objects.all()
    }
    return render(request,'bmi/all.html',params)