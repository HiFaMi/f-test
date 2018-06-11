from django.conf.urls import url
from django.urls import path
from .views import school_list

urlpatterns = [
    url(r'^school/', school_list)
]
