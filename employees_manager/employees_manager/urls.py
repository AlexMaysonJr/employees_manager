"""
URL configuration for employees_manager project.

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django_registration.backends.activation.views import RegistrationView
from custom_authentication.forms import CustomRegistrationForm
import custom_authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/profile/', custom_authentication.views.profile, name='profile'),
    path('accounts/register/', RegistrationView.as_view(form_class=CustomRegistrationForm), name='django_registration_register'),
    path('', RedirectView.as_view(url='/accounts/profile'))
]
