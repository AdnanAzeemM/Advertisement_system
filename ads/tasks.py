from celery import shared_task
from .models import Advertisement
from datetime import datetime
from utils.generate_advertisement_report import generate_excel_report
import os


@shared_task
def reset_daily_visitors():
    now = datetime.now()
    active_ads = Advertisement.objects.filter(ad__end_date__gte=now)
    if active_ads.exists():
        try:
            generate_excel_report(active_ads)
            active_ads.update(daily_visitors=0, blocked=False)
            print("Successfully reset daily visitors count for all ad locations")
        except Exception as e:
            print(f"Error resetting daily visitors count: {e}")
