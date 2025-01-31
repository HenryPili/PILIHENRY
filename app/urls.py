from django.urls import path
from .views import (HomePageView, AboutPageView, ProjectsPageView, GarbageScheduleListView,
                    GarbageScheduleDetailView, GarbageScheduleCreateView, GarbageScheduleUpdateView, GarbageScheduleDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('Projects/', ProjectsPageView.as_view(), name='Projects'),
    path('GarbageSchedule/', GarbageScheduleListView.as_view(), name='GarbageSchedule'),  # Correct endpoint for list view
    path('GarbageSchedule/<int:pk>/', GarbageScheduleDetailView.as_view(), name='GarbageSchedule_detail'),  # Added trailing slash for consistency
    path('GarbageSchedule/create/', GarbageScheduleCreateView.as_view(), name='GarbageSchedule_create'),  # Added trailing slash
    path('GarbageSchedule/<int:pk>/edit/', GarbageScheduleUpdateView.as_view(), name='GarbageSchedule_update'),  # Added trailing slash
    path('GarbageSchedule/<int:pk>/delete/', GarbageScheduleDeleteView.as_view(), name='GarbageSchedule_delete'),  # Added trailing slash
]
