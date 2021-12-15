from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_view, name = "add"),
    path('update_task/<int:pk>', views.update_task_view, name = "update_task"),
    path('remove/<int:pk>', views.remove_view, name = "remove"),
]
