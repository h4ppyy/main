from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews

urlpatterns = [
    path('', SampleViews.sample, name='sample'),
    path('login', LoginViews.login, name='login'),
]
