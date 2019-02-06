from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from testapp.models import Membership
from testapp.forms import MembershipForm


 #Create your views here.
def home_page_view(request):
    return render(request, 'testapp/home.html')
#def base_page_view():
    #return render(request, 'testapp/base.html')

#def Showfullname(request):
   # fullname =  request.user.get_full_name()
   # context = {'fullname':fullname}
    #return render(request, 'testapp/welcome.html', context)

def welcome_view(request):
    username = request.user.username
    return render(request, 'testapp/welcome.html', {'username': username})


def logout_view(request):
    return render(request, 'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form':form })


def retrieve_view(request):
    members = Membership.objects.all()
    return render(request, 'testapp/dashboard.html', {'members': members })

def create_view(request):
    form=MembershipForm()
    if request.method =='POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'testapp/confirmation.html')
    return render(request, 'testapp/membership.html', {'form': form})

def delete_view(request, id):
    member =Membership.objects.get(id = id)
    member.delete()
    return render(request, 'testapp/cancellation.html' )

def update_view(request, id):
    member =Membership.objects.get(id = id)
    if request.method=='POST':
        form = MembershipForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return render(request, 'testapp/updated.html')

    return render(request, 'testapp/update.html', {'member': member})
