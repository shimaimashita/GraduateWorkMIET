from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('asking/new/', views.post_new, name='post_new'),
    path('asking/mailing/', views.mailing_new, name='mailing_new'),
    path('asking/statistic/', views.statistic_new, name='statistic_new'),
]
