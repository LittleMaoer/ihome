from django.shortcuts import render

from common.models import House


def search(request):
    if request.method == 'GET':
        return render(request, 'renter/search.html')


def detail(request, id):
    if request.method == 'GET':
        house = House.objects.filter(id=id).first()
        return render(request, 'renter/detail.html', {'house': house})


def booking(request, id):
    if request.method == 'GET':
        house = House.objects.filter(id=id).first()
        return render(request, 'renter/booking.html', {'house': house})


def orders(request):
    if request.method == 'GET':
        return render(request, 'renter/orders.html')

