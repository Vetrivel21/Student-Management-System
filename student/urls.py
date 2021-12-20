from django.urls import path
from .import views
urlpatterns = [
    path('api/student/', views.student_list.as_view(), name='student-list'),
    path('api/student/<int:pk>/', views.student_details, name='student-details'),
]
