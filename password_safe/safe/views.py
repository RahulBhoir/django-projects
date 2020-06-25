from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PasswordSafe


def home(request):
    if request.method == 'POST':
        s_name = request.POST.get('site_name')
        u_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = User.objects.get(id=request.user.id)
        db = PasswordSafe(site_name=s_name, username=u_name,
                          password=password, owner=user)
        db.save()
        messages.success(request, f'Account details saved.')
        return redirect('safe-home')
    else:
        return render(request, 'safe/home.html')


@login_required
def display(request):
    db = PasswordSafe.objects.filter(owner_id=request.user.id)
    if db is None:
        context = {'database': None}
    else:
        context = {'database': db}
    return render(request, 'safe/display.html', context)


def showPassword(request, item_id):
    item = PasswordSafe.objects.get(id=item_id)
    context = {
        'website': item.site_name,
        'username': item.username,
        'password': item.password
    }
    return render(request, 'safe/show.html', context)


def deletePassword(request, item_id):
    item = PasswordSafe.objects.get(id=item_id)
    item.delete()
    return redirect('display-password')


def updateDetails(request, item_id):
    if request.method == 'POST':
        s_name = request.POST.get('site_name')
        u_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = User.objects.get(id=request.user.id)

        db = PasswordSafe.objects.filter(id=item_id).update(
            site_name=s_name, username=u_name, password=password,
            owner=user)
        return redirect('display-password')
    else:
        item = PasswordSafe.objects.get(id=item_id)
        context = {
            'item': item
        }
        return render(request, 'safe/update.html', context)
