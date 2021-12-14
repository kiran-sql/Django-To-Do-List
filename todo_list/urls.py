from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_view, name = "add"),
    path('add/', views.add_view, name = "add"),
    path('remove/', views.remove_view, name = "remove"),
]
