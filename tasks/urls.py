from django.urls import path, include
from rest_framework import routers

from tasks.views import TaskView, TimeslotView, TimeslotGetView, TaskButtonView,TaskStatusView

router = routers.DefaultRouter()
router.register('task', TaskView)


urlpatterns = [
    path('', include(router.urls)),
    path('time/<int:pk>/', TimeslotView.as_view()),
    path('time/', TimeslotGetView.as_view()),
    path('task-status/', TaskStatusView.as_view()),
    path('task-button/<int:pk>/', TaskButtonView.as_view()),
]