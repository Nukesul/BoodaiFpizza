from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админки
    path('api/', include('shop.urls')),  # Маршрут для API (приложение shop)
]

# Добавляем маршруты для статических и медиафайлов (например, для изображений пицц)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)