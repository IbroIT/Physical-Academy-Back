from django.urls import path
from . import views

app_name = 'banner'

urlpatterns = [
    path('slides/', views.BannerSlideListAPIView.as_view(), name='banner-slides'),
]