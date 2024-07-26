from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdViewSet,
    LocationViewSet,
    AdvertisementListView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementDeleteView,
    AdvertisementDetailView,
)

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'locations', LocationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('advertisement/', AdvertisementListView.as_view(), name='advertisement-list'),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement-detail'),

    path('advertisement/create/', AdvertisementCreateView.as_view(), name='advertisement-create'),
    path('advertisement/update/<int:pk>/', AdvertisementUpdateView.as_view(), name='advertisement-update'),
    path('advertisement/delete/<int:pk>/', AdvertisementDeleteView.as_view(), name='advertisement-delete'),
]