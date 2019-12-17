from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import static
from news.views import WebService, WebService1
from news.api import NewsAPIView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/test', WebService.as_view()),
    path('api/test1', WebService1.as_view()),
    path('api/test2', NewsAPIView.as_view()),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
