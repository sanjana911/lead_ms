"""
URL configuration for lead_ms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import SignUpView
from rest_framework.authtoken.views import ObtainAuthToken
from accounts.views import UserDetailView
from leads.views import LeadListCreateView
from leads.views import LeadRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/register/',SignUpView.as_view()),
    path('api/accounts/login/',ObtainAuthToken.as_view()),
    path('api/accounts/profile/',UserDetailView.as_view()),
    path('api/leads/',LeadListCreateView.as_view()),
    path('api/leads/<int:pk>/',LeadRetrieveUpdateDeleteView.as_view()),
    
    
]
