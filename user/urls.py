from django.urls import path, include
from .views import register_page,login_page, verify_email_confirm

app_name = 'user'

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm'),

]