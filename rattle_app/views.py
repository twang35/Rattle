from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from rattle_app.forms import AuthenticateForm, UserCreateForm, RattleForm
from rattle_app.models import Rattle
from django.contrib.auth.decorators import login_required

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')
 
 
def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

@login_required
def submit(request):
    if request.method == "POST":
        rattle_form = RattleForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if rattle_form.is_valid():
            rattle = rattle_form.save(commit=False)
            rattle.user = request.user
            rattle.save()
            return redirect(next_url)
        else:
            return public(request, rattle_form)
    return redirect('/')

@login_required
def public(request, rattle_form=None):
    rattle_form = rattle_form or RattleForm()
    rattles = Rattle.objects.reverse()[:10]
    return render(request,
                  'public.html',
                  {'rattle_form': rattle_form, 'next_url': '/rattles',
                   'rattles': rattles, 'username': request.user.username})

