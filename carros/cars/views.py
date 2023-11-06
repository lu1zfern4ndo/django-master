from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search)
    return render(request, 'cars/cars.html', context={'cars': cars})


def new_car(request):
    if request.method == 'POST':
        new_car = CarForm(request.POST, request.FILES)
        if new_car.is_valid():
            new_car.save()
            return redirect('cars_list')
    elif request.method == 'GET':
        new_car = CarForm()
    return render(request, 'cars/new_car.html', context={ 'new_car': new_car })
