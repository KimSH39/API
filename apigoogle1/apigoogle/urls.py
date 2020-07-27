from django.contrib import admin
from django.urls import path
import googleapi.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',googleapi.views.home,name='home'),
    ]
