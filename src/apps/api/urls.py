from django.urls import re_path, include
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register('rusers', UserViewSet, basename='users')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
