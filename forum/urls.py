from django.urls import path
from forum import views
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', ForumListView.as_view(), name='list'),
    path('<int:pk>/', ForumDetailView.as_view(), name='detail'),
    path('add/', ForumCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', ForumUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ForumDeleteView.as_view(), name='delete'),
]