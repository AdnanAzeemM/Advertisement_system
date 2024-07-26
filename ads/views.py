from rest_framework import viewsets
from .forms import LocationForm, AdForm, AdvertisementForm
from .models import Ad, Location, Advertisement
from .serializers import AdSerializer, LocationSerializer, AdvertisementSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
import logging
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        location = self.request.query_params.get('location', None)
        if location:
            return Advertisement.objects.filter(location__name__icontains=location, blocked=False)
        return Advertisement.objects.filter(blocked=False)


class AdvertisementDetailView(generics.RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.daily_visitors < instance.location.max_visitors:
            instance.daily_visitors += 1
            instance.save()
        else:
            instance.blocked = True
            instance.save()
            return Response(
                {"message": "Advertisement reached its limit and is now blocked."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AdvertisementCreateView(generics.CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementUpdateView(generics.UpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementDeleteView(generics.DestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


######### Templates View ##################


def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = LocationForm()
    return render(request, 'location/location_form.html', {'form': form})


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location/location_list.html', {'locations': locations})


def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'location/location_detail.html', {'location': location})


def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/location_form.html', {'form': form, 'update': True})


def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('location-list')
    return render(request, 'locations/location_confirm_delete.html', {'location': location})


def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad-list')
    else:
        form = AdForm()
    return render(request, 'ad/ad_form.html', {'form': form})


def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ad/ad_list.html', {'ads': ads})


def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'ad/ad_detail.html', {'ad': ad})


def ad_update(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad-list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ad/ad_form.html', {'form': form, 'update': True})


def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ad-list')
    return render(request, 'ad/ad_confirm_delete.html', {'ad': ad})


def advertisement_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advertisement-list')
    else:
        form = AdvertisementForm()
    return render(request, 'advertisement/advertisement_form.html', {'form': form})


def advertisement_list(request):
    advertisements = Advertisement.objects.filter(blocked=False)
    location = request.GET.get('location')
    if location:
        advertisements = advertisements.filter(location__name__icontains=location)
    return render(request, 'advertisement/advertisement_list.html', {'advertisements': advertisements})


def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if advertisement.daily_visitors < advertisement.location.max_visitors:
        advertisement.daily_visitors += 1
        advertisement.save()
    else:
        advertisement.blocked = True
        advertisement.save()
        return render(request, 'advertisement/advertisement_detail.html', {
            'advertisement': advertisement,
            'error_message': 'Advertisement reached its limit and is now blocked.'
        })
    return render(request, 'advertisement/advertisement_detail.html', {'advertisement': advertisement})


def advertisement_update(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('advertisement-list')
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'advertisement/advertisement_form.html', {'form': form, 'update': True})


def advertisement_delete(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        advertisement.delete()
        return redirect('advertisement-list')
    return render(request, 'advertisement/advertisement_confirm_delete.html', {'advertisement': advertisement})
