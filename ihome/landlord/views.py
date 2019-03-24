from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from common.forms import HouseForm
from common.models import User, House, Area


def myhouse(request):
    if request.method == 'GET':
        user = User.objects.filter(id=request.session['user_id']).first()
        houses = user.house_set.all()
        return render(request, 'landlord/myhouse.html', {'houses': houses, 'user': user})


def auth(request):
    if request.method == 'GET':
        return render(request, 'landlord/auth.html')
    if request.method == 'POST':
        user = User.objects.filter(id=request.session['user_id']).first()
        user.id_name = request.POST['real_name']
        user.id_card = request.POST['id_card']
        user.save()
        return HttpResponseRedirect(reverse('landlord:my'))


def profile(request):
    if request.method == 'GET':
        user = User.objects.filter(id=request.session['user_id']).first()
        return render(request, 'landlord/profile.html', {'user': user})
    if request.method == 'POST':
        user = User.objects.filter(id=request.session['user_id']).first()
        user.avatar = request.FILES.get('avatar')
        name = request.POST.get('name')
        user.name = name
        user.save()
        return HttpResponseRedirect(reverse('landlord:my'))


def my(request):
    if request.method == 'GET':
        user = User.objects.filter(id=request.session['user_id']).first()
        return render(request, 'landlord/my.html', {'user': user})
    # if request.method == 'POST':
    #     user = User.objects.filter(id=request.session['user_id']).first()
    #     return HttpResponseRedirect(reverse('landlord:profile', {'user': user}))


def newhouse(request):
    if request.method == 'GET':
        return render(request, 'landlord/newhouse.html')
    if request.method == 'POST':
        user = User.objects.filter(id=request.session['user_id']).first()
        houses = user.house_set

        form = HouseForm(request.POST)
        if form.is_valid():
            house = House.objects.create(
                                    user_id_id=request.session['user_id'],
                                    title=form.cleaned_data['title'],
                                    price=form.cleaned_data['price'],
                                    area_id=Area.objects.filter(pk=form.cleaned_data['area_id']).first(),
                                    address=form.cleaned_data['address'],
                                    room_count=form.cleaned_data['room_count'],
                                    acreage=form.cleaned_data['acreage'],
                                    unit=form.cleaned_data['unit'],
                                    capacity=form.cleaned_data['capacity'],
                                    beds=form.cleaned_data['beds'],
                                    deposit=form.cleaned_data['deposit'],
                                    min_days=form.cleaned_data['min_days'],
                                    max_days=form.cleaned_data['max_days'],
                                    )
            house.save()
            return HttpResponseRedirect(reverse('landlord:myhouse'), {'houses': houses})
        else:
            errors = form.errors
            return render(request, 'landlord/newhouse.html', {'errors':errors})


def lorders(request):
    if request.method == 'GET':

        return render(request, 'landlord/lorders.html')
