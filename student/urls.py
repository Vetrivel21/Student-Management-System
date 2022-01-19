from django.urls import path
from .import views
urlpatterns = [
    path('api/student/',  views.student_list.as_view(),  name='student-list'),
    path('api/student/sort/page/',  views.student_LIST.as_view(),  name='student-LIST'),
    path('api/student/filter/', views.student_filter.as_view(), name='student-filter'),
    path('api/student/<int:pk>/', views.student_details, name='student-details'),
]
