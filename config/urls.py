from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upskill/', include('upskill.urls', namespace='upskill')),
    path('user/', include('user.urls', namespace='user')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)