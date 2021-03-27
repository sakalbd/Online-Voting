from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_test_home_page),
    path('info/', views.show_test1_info_page)


]