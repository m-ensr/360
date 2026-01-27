from django.urls import path
from .views import (
    HomeView,
    MeetingCreateView,
    MeetingDetailView,
    MeetingActiveView,
    MeetingCompletedView,
    TasksView,
    TaskCompletedView,
    TaskCreateView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='toplanti_home'),
    path('<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),
    path('olustur/', MeetingCreateView.as_view(), name='meeting_create'),
    path('aktif/', MeetingActiveView.as_view(), name='meeting_active'),
    path('tamamlanan/', MeetingCompletedView.as_view(), name='meeting_completed'),
    # Görev
    path('gorevler/', TasksView.as_view(), name='tasks'),
    path('gorevler/olustur/', TaskCreateView.as_view(), name='tasks_create'),
    path('gorevler/tamamlanan/', TaskCompletedView.as_view(), name='task_completed'),
]
