from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventListAPI

router = DefaultRouter()
router.register(r'', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
    path('', EventListAPI.as_view(), name='event-list'),
]