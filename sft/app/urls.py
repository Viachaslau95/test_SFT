from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import ContractViewSet

router = DefaultRouter()

router.register('contracts', ContractViewSet)


urlpatterns = [
    path('', include(router.urls)),
]