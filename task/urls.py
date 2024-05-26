from django.urls import path
from task.views import *


urlpatterns=[
    path("signup",RegistrationView.as_view(),name="signup"),
    path("login",LoginView.as_view(),name="login"),
    path("task/add",TaskAddView.as_view(),name="task-add"),
    path("task/list",TaskListView.as_view(),name="task-list"),
    path("task/<int:pk>/delete",DeleteView.as_view(),name="task-delete"),
    path("task/<int:pk>/update",UpdateTaskView.as_view(),name="task-update"),
    path("task/<int:pk>/detail",DetailTaskView.as_view(),name="task-detail")


]