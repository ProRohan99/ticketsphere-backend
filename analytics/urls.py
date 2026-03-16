from django.urls import path
from .views import AnalyticsDashboardAPI

urlpatterns = [
    path('dashboard/', AnalyticsDashboardAPI.as_view(), name='analytics-dashboard'),
]