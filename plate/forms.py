from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car  # 사용할 모델
        fields = ['car_num', 'car_image']  # CarForm에서 사용할 Car 모델의 속성
        widgets = {
            'car_num': forms.TextInput(attrs={'class': 'form-control'}),
            'car_image': forms.ImageField(),
        }