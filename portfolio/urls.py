"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from architect import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home'),

    #CV download
    path('download-cv/', views.Download_CV, name='download_cv'),

    #Contact me
    path('contact/', views.contact_form, name='contact-form'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
