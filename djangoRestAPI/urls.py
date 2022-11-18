from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('api/', include(router.urls))
]

