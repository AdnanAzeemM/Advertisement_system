from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    max_visitors = models.IntegerField()
    latitude = models.DecimalField(decimal_places=6, max_digits=10, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    daily_visitors = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('ad', 'location')

    def __str__(self):
        return f"{self.ad.name} - {self.location.name}"
