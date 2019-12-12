import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.conf import settings
from backend.djangoapps.common.views import *


def sample(request):
    context = {}
    return render(request, 'sample/sample.html', context)


def api_sample(request):
    return JsonResponse({'result': 200})
