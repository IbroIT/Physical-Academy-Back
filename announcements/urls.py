from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.AnnouncementListAPIView.as_view(), name='announcement-list'),
    path('<int:id>/', views.AnnouncementDetailAPIView.as_view(), name='announcement-detail'),
]