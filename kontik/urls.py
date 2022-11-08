from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('knigi/', include('knigi.urls')),
    path('admin/', admin.site.urls),
]