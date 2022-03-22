from datetime import date, timedelta, timezone


def date_processor(request):
    global_date = date.today()
    return {"global_date": global_date}
