from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='glavnaya'),
    path('<str:slug>/', GetPost.as_view(), name='post'),


    #path('category/<str:slug>/', get_category, name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),

]

