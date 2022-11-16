from .models import Car
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect
from .forms import CarForm
from django.utils import timezone
# Create your views here.



def index(request): # 기본 페이지
  page = request.GET.get('page', '1')  # 페이지
  car_list = Car.objects.order_by('car_num')
  paginator = Paginator(car_list, 1)  # 페이지당 1개씩 보여주기
  page_obj = paginator.get_page(page)
  context = {'car_list': page_obj}
  return render(request, 'plate/index.html', context)


def plate_create(request): # 차 등록
  if request.method == 'POST':
    car = Car()
    car.car_num = request.POST['car_num'] # 차 번호
    car.car_image = request.FILES['car_image'] # 차 이미지

    car.save()
    return redirect('plate:index')  # 메인 페이지

  else:
    form = CarForm()
  context = {'form': form}
  return render(request, 'plate/form.html', context) # 폼 페이지

