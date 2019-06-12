import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


def login(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    return render(request, 'login/login.html', context)
    #return JsonResponse({'a':'b'})
