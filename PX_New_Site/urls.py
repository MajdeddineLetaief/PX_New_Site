from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('PX_Site_App.urls')),
    path('admin/', admin.site.urls),]