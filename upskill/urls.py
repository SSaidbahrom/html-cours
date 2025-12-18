from django.urls import path
from .views import IndexView, about, course, course_detail

app_name = 'upskill'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('course/', course, name='course'),
    path('about/', about, name='about'),
    path('course/<slug:subject_slug>/', course, name='course_by_subject'),
    path('course/<slug:slug>/', course_detail, name='course'),
]

