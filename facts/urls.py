from django.urls import path
from . import views

app_name = 'facts'

urlpatterns = [
    path('', views.FactListAPIView.as_view(), name='fact-list'),
]