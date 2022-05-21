from django.contrib import admin
from django.urls import path, include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth', include('rest_framework.urls')),
    re_path('api/v1/rest-auth/', include('rest_auth.urls')),
]
