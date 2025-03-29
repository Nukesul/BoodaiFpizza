from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, CategoryViewSet, PizzaViewSet, OrderViewSet

# Создаем роутер для DRF
router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'pizzas', PizzaViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Подключаем все маршруты из роутера
]