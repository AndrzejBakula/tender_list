from datetime import date, timedelta, timezone
from django.utils import timezone


def date_processor(request):
    global_date = timezone.localtime(value=None, timezone=None).date()
    # global_date = f"{part_date.strftime('%A')} {part_date}"
    return {"global_date": global_date}
