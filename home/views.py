from django.shortcuts import render
from django.http import HttpResponse
from .models import Training

# Create your views here.
##def homepage(self):
##    return HttpResponse('<h1>First day with Django!</h1>')

def homepage(self):
    return render(request=self, template_name='home/index.html',
                  context = {"training":Training.objects.all()})
