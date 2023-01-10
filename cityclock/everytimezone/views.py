from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from datetime import datetime
from django.utils import timezone

common_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
    "Chennai": "Asia/Calcutta",
}

format = "%H:%M:%S"


def home(request):
    return render(
        request,
        "time/home.html",
        {
            "city": settings.DEFAULT_CITY,
            "time": str(
                datetime.now(timezone.get_current_timezone()).strftime(format)
            ),
        },
    )


def set_timezone(request):
    if request.method == "POST":
        request.session["django_timezone"] = request.POST["timezone"]
        settings.TIME_ZONE = request.POST["timezone"]
        settings.DEFAULT_CITY = get_city(request.POST["timezone"])
        return redirect(reverse("home"))
    else:
        return render(
            request, "time/time.html", {"timezones": common_timezones}
        )


def get_city(timeZone):
    for city, zone in common_timezones.items():
        if zone == timeZone:
            return city
    return " "
