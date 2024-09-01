from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import NormalSignUpForm,NormalLoginForm,ContributorSignUpForm,ContributorLoginForm
from general.models import NormalUser,Contributor,User
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request, "generalhome.html", {})


class NormalSignUpView(CreateView):
    model = User
    form_class = NormalSignUpForm
    template_name = 'signuppageuser.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'normal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user/homepage')
    
def normalLogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    form=NormalLoginForm()
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_normal:
        login(request, user)
        return redirect("user/homepage")
    else:
        return render(request, "loginpageuser.html", {'form':form})
    
class ContributorSignUpView(CreateView):
    model = User
    form_class = ContributorSignUpForm
    template_name = 'signuppagecontributor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'contributor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('contributor/homepage')
    
def contributorLogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    form=ContributorLoginForm()
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_contributor:
        login(request, user)
        return redirect("contributor/homepage")
    else:
        return render(request, "loginpagecontributor.html", {'form':form})
    
def aboutPage(request):
    return render(request, "aboutPage.html")
    
