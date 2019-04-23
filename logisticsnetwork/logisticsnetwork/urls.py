from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.http import HttpResponse

ping_view = lambda request: HttpResponse('pong!')

urlpatterns = [
    url(r'', include('logistics.urls')),
    url(r'ping/', ping_view),
    path('admin/', admin.site.urls),
]
