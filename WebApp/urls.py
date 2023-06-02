from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about us/", views.aboutUs, name="about us"),
    path("forgot password/", views.forgotPassword, name="forgot password"),
    path("home page 2/", views.home2, name="home page 2"),
    path("home page 3/", views.home3, name="home page 3"),
    path("database/", views.database, name="database"),
    path("notifications/", views.notifications, name="notifications"),
    path("notifications page 2/", views.notifications2, name="notifications page 2"),
    path("tickets/", views.tickets, name="tickets"),
    path("tickets page 2/", views.tickets2, name="tickets page 2"),
    path("tickets page 3/", views.tickets3, name="tickets page 3"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
