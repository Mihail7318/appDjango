from django.urls import path
from .views import *

urlpatterns = [
    path('board_of_trustees/', board_of_trustees.as_view(), name='board_of_trustees'),
    path('get_one_board_of_trustees/<str:slug>/', get_one_board_of_trustees.as_view(), name='get_one_board_of_trustees'),
    path('expert_council/', expert_council.as_view(), name='expert_council'),
    path('get_one_expert_council/<str:slug>/', get_one_expert_council.as_view(), name='get_one_expert_council'),

]

