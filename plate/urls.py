from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from plate import views

app_name = 'plate'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/', views.plate_create, name='plate_create'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)