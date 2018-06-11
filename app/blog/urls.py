from django.conf.urls import url
from django.urls import path
from .views import school_name

urlpatterns = [
    url(r'^school/', school_name)
]
