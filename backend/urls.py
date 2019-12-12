from django.urls import path
from django.conf.urls import url
from .djangoapps.sample import views as SampleViews
from .djangoapps.login import views as LoginViews


urlpatterns = [
    # Render
    path('', SampleViews.sample, name='sample'),
    path('login', LoginViews.login, name='login'),

    # Rest Api
    path('api/v1/sample', SampleViews.api_sample, name='api_sample'),
]
