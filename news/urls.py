from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('', views.NewsAPIView.as_view(), name='get-post-data')
]
