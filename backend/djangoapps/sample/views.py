import json
import requests
import cv2
import uuid
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
    # create qr code
    u1 = str(uuid.uuid4()).replace('-', '')
    file_name = u1 + '.png'
    url = 'https://chart.apis.google.com/chart?cht=qr&chs=150x150&chl=hello'
    response = requests.get(url)
    with open(settings.BANNER_PATH + 'history/' + file_name, 'wb') as f:
        f.write(response.content)

    # merge post, qr code
    BASE = cv2.imread(settings.BANNER_PATH + 'base.jpg', 1)
    QR = cv2.imread(settings.BANNER_PATH + 'history/' + file_name, 1)
    BASE = cv2.resize(BASE, dsize=(500, 700), interpolation=cv2.INTER_AREA)
    QR = cv2.resize(QR, dsize=(100, 100), interpolation=cv2.INTER_AREA)
    x_offset = 390
    y_offset = 585
    BASE[y_offset:y_offset + QR.shape[0], x_offset:x_offset + QR.shape[1]] = QR
    u2 = str(uuid.uuid4()).replace('-', '')
    file_name = u2 + '.png'
    cv2.imwrite(settings.BANNER_PATH + 'history/' + file_name, BASE) 

    return JsonResponse({'result': file_name})
