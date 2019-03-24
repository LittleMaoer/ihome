from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from common.forms import UserForm, LoginForm
from common.models import User


def index(request):
    if request.method == 'GET':
        return render(request, 'common/index.html')
    if request.method == 'POST':
        pass


def register(request):
    if request.method == 'GET':
        return render(request, 'common/register.html')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(phone=form.cleaned_data['mobile'],
                                pwd_hash=form.cleaned_data['password'])
            return HttpResponseRedirect(reverse('common:login'))
        errors = form.errors
        return render(request, 'common/register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'common/login.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() and form.errors == {}:
            user = User.objects.filter(phone=form.cleaned_data.get('mobile')).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('common:checked_index'))
        errors = form.errors
        return render(request, 'common/login.html', {'errors': errors})


def checked_index(request):
    if request.method == 'GET':
        return render(request, 'common/checked_index.html')
    if request.method == 'POST':
        pass

