from django.urls import path, include
from . import views
from rest_framework import routers
#routers allows to GET, POST requests

router = routers.DefaultRouter()
router.register('wdapi', views.WDAPIView)

urlpatterns = [
    path('', include(router.urls))   
]
