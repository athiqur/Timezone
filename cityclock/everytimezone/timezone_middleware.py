from backports.zoneinfo import ZoneInfo
from django.utils import timezone
from everytimezone.views import common_timezones
from django.conf import settings


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(ZoneInfo(tzname))
            settings.DEFAULT_CITY = request.session.get("django_city")
        else:
            settings.DEFAULT_CITY = "Chennai"
            timezone.deactivate()
        return self.get_response(request)
