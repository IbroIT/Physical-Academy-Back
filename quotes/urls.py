from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.QuoteListAPIView.as_view(), name='quote-list'),
]