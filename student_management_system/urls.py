from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('', include('admin_account.urls')),
]

