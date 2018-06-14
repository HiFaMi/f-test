from django.conf.urls import url

from .views import school_list, school_detail, student_list, student_detail

urlpatterns = [
    url(r'^school/$', school_list),
    url(r'^school/(\d)+/$', school_detail),
    url(r'^students/$', student_list),
    url(r'^students/(\d)+/$', student_detail),
]
