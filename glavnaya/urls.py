from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
       path('slider/', slider),
       path('', Home.as_view(), name='glavnaya'),

]
