from django.urls import path
from projects import views

urlpatterns = [
    path('test', views.project_list),
]
