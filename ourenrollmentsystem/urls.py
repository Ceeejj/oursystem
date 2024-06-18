from django.urls import path
from .import views

urlpatterns = [
    path('level',views.index_level),
    path('level/create', views.create_level),
    path('level_store', views.store_level),
    path('students', views.index_student),
    path('students/create', views.create_user),
]
