from django.urls import path
from . import views

urlpatterns = [
    path('allteachers/', views.teacher_list, name='teacher_list'),
    path('<int:teacher_id>/', views.single_teacher, name='single_teacher'),
    path('registration/', views.create_teacher, name='create_teacher'),
    path('edit/<int:pk>', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
]

