from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, ListView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Parts


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

def login_user(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            error_message = "Bunday foydalanuvchi topilmadi!"
        else:
            user = authenticate(request, username=username, password=password)
            if user is None:
                error_message = "Parol noto‘g‘ri!"
            else:
                login(request, user)
                return redirect('parts-list')

    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form, 'error_message': error_message})

def logout_user(request):
    logout(request)
    return redirect('login')

def login_profile(request):
    return render(request, 'profile.html')

class UserUpdate(UpdateView):
    model = User
    form_class = RegisterForm
    template_name = 'update_user.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('home')


class SearchList(View):
    def get(self, request):
        query = request.GET.get('t', '')
        products = Parts.objects.filter(name__icontains=query) if query else None
        return render(request, 'search.html', {'products': products})

class PartsList(ListView):
    model = Parts
    template_name = 'parts_list.html'
    context_object_name = 'parts'
