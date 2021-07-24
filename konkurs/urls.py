from django.urls import path

from .views import *

urlpatterns = [
    path('fed/', fed),
    path('reg/', reg),

]
