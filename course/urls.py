from sys import path
from django import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]