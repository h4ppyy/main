import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


def login(request):
    context = {}
    return render(request, 'login/login.html', context)
