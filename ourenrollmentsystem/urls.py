from django.urls import path
from .import views

urlpatterns = [
    path('level',views.index_level),
    path('level/create', views.create_level),
    path('level_store', views.store_level),
    path('students', views.index_student),
    path('students/create', views.create_user),
    path('students/log_in', views.login_view),
    path('students/store', views.store_students),
    path('students/show/<int:user_id>', views.show_info,),
    path('students/update/<int:level_id>', views.update_students),
]
