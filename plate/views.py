from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Admin, Car

# Create your views here.
def index(request):
  car_list = Car.objects.order_by('car_num')
  context = {'car_list': car_list}
  return render(request, 'plate/index.html', context)