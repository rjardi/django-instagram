from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

from instagram.forms import RegistrationForm
from django.contrib import messages

class HomeView(TemplateView) :
    template_name = "general/home.html"

class LoginView(TemplateView):
    template_name = "general/login.html"

class RegisterView(CreateView) :
    template_name = "general/register.html"
    model=User
    success_url=reverse_lazy("login")
    form_class=RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente.")
        return super(RegisterView, self).form_valid(form)

class LegalView(TemplateView) :
    template_name = "general/legal.html"

class ContactView(TemplateView) :
    template_name = "general/contact.html"