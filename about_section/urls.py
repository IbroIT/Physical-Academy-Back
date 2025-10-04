from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'leadership', views.LeadershipViewSet, basename='leadership')
router.register(r'accreditations', views.AccreditationViewSet, basename='accreditation')
router.register(r'organization-structure', views.OrganizationStructureViewSet, basename='organization-structure')
router.register(r'documents', views.DownloadableDocumentViewSet, basename='downloadable-document')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
    
    # Custom endpoints
    path('leadership/directors/', views.LeadershipViewSet.as_view({'get': 'directors'}), name='leadership-directors'),
    path('leadership/department-heads/', views.LeadershipViewSet.as_view({'get': 'department_heads'}), name='leadership-department-heads'),
    path('accreditations/active/', views.AccreditationViewSet.as_view({'get': 'active'}), name='accreditations-active'),
    path('organization-structure/hierarchy/', views.OrganizationStructureViewSet.as_view({'get': 'hierarchy'}), name='organization-structure-hierarchy'),
]