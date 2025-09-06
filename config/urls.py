from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# Media fayllarni DEBUG bo‘lsin yoki bo‘lmasin xizmat qilish
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
