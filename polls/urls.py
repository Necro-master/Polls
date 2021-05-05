from django.urls import path
from . import views

urlpatterns = [
    path('', views.polls_list, name='poll_  list'),
    path('poll/<int:poll_id>/', views.poll_page, name='poll_page'),
    path('endpage', views.end_page, name='end_page'),
    path('poll/<int:poll_id>/answers', views.answer_list),
    path('poll/<int:poll_id>/answers/<int:answer_id>', views.answer_page),
]