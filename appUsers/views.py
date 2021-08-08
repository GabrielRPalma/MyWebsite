from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appUsers.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from curriculum.models import Standard, Lesson
# Create your views here.


def index(request):

    return render(request, 'index.html')


def dashboard(request):
    modules = len(Standard.objects.all())
    lessons = len(Lesson.objects.all())

    return render(request, 'curriculum/dashboard.html', {'modules': modules, 'lessons':lessons})


def discover(request):

    return render(request, 'appUsers/discover.html')


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'appUsers/register.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('appUsers:dashboard'))
            else:
                return HttpResponse('ACCOUNT IS DEACTIVATED')

        else:
            return HttpResponse('Please use a correct username and password')

    else:

        return render(request, 'appUsers/join.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('appUsers:index'))
