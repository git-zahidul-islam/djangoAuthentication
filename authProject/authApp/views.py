from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# for class base view [CBV]
from django.views import View
# import the user class (model)
from django.contrib.auth.models import User
# import the register form 
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username,password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()  # Initialize a blank form for GET requests
    
    # Always render the form, either blank or pre-filled, for GET and invalid POST
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    error_messages = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the 'next' page if provided, or to 'home' by default
            next_page = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_page)
        else:
            error_messages = "Invalid Credential"
            
    return render(request, 'accounts/login.html', {'error': error_messages})

            


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')



# home view
# useing the decorator
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')

# protceted views
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - redirect url
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')
