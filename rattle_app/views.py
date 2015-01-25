from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from rattle_app.forms import AuthenticateForm, UserCreateForm, RattleForm
from rattle_app.models import Rattle

def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        rattle_form = RattleForm()
        user = request.user
        rattles_self = Rattle.objects.filter(user=user.id)
        rattles_buddies = Rattle.objects.filter(user__userprofile__in=user.profile.follows.all)
        rattles = rattles_self | rattles_buddies
 
        return render(request,
                      'buddies.html',
                      {'rattle_form': rattle_form, 'user': user,
                       'rattles': rattles,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()
 
        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })