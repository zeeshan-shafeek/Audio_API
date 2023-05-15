
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

# Register the UserAudioViewSet with the router for the 'user-audio' endpoint.
router.register(r'user-audio', views.UserAudioViewSet)

# Register the SolutionViewSet with the router for the 'solution' endpoint.
router.register(r'solution', views.SolutionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]