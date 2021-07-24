from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    #path('setting/', Setting),

    path('faq/', faq),
    path('privacypolicy/', privacypolicy),
    path('contacts/', contact),
    path('aboutus/', aboutus),
    path('useragreement/', useragreement),

]
