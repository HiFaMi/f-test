from django.http import HttpResponse
from django.shortcuts import render
from .models import School,Student


def school_name(request):
    schools = School.objects.all()

    return HttpResponse(schools)
