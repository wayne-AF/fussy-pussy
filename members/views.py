from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')








def homepage(request):
    return render(request, 'index.html')
