"""advertisement_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from ads.views import location_list, location_detail, ad_list, ad_detail, advertisement_list, advertisement_detail, \
    location_create, ad_create, advertisement_create, location_update, location_delete, ad_update, ad_delete, \
    advertisement_update, advertisement_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ads.urls')),
    path('locations/create/', location_create, name='location-create'),
    path('locations/', location_list, name='location-list'),
    path('locations/<int:pk>/', location_detail, name='location-detail'),

    path('locations/<int:pk>/update/', location_update, name='location-update'),
    path('locations/<int:pk>/delete/', location_delete, name='location-delete'),
    path('ads/create/', ad_create, name='ad-create'),
    path('ads/', ad_list, name='ad-list'),
    path('ads/<int:pk>/', ad_detail, name='ad-detail'),

    path('ads/<int:pk>/update/', ad_update, name='ad-update'),
    path('ads/<int:pk>/delete/', ad_delete, name='ad-delete'),
    path('advertisements/create/', advertisement_create, name='advertisement-create'),
    path('advertisements/', advertisement_list, name='advertisement-list'),
    path('advertisements/<int:pk>/', advertisement_detail, name='advertisement-detail'),
    path('advertisements/<int:pk>/update/', advertisement_update, name='advertisement-update'),
    path('advertisements/<int:pk>/delete/', advertisement_delete, name='advertisement-delete'),
    path('api-auth/', include('rest_framework.urls'))
]
