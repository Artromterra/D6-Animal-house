"""enimallapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from animal_data import views
from animal_data.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('index/', views.index, name='index'),
	path('', HomeView.as_view(), name='home'),
	path('dog_list/', views.dog_list, name='dog_list'),
	path('dog/<int:pk>/', views.dog, name='dog'),
	path('cat_list/', views.cat_list, name='cat_list'),
	path('cat/<int:pk>/', views.cat, name='cat'),
	path('parrot_list/', views.parrot_list, name='parrot_list'),
	path('parrot/<int:pk>/', views.parrot, name='parrot'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)