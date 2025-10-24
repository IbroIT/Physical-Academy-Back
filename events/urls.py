from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
    path('events/featured/', views.FeaturedEventListAPIView.as_view(), name='featured-events'),
    path('events/categories/', views.EventCategoryListAPIView.as_view(), name='event-categories'),
    path('events/departments/', views.EventDepartmentListAPIView.as_view(), name='event-departments'),
]