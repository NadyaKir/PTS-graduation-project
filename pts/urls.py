
from cgitb import handler
from django.conf import settings
from django.contrib import admin
from django.urls import path
from news.views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),


]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "news.views.pageNotFound"
