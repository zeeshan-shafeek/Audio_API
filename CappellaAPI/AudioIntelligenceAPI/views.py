from django.shortcuts import render
from rest_framework import viewsets

from .serializer import UserAudioGetSerializer, UserAudioPostSerializer, SolutionGetSerializer
from .models import UserAudio


class UserAudioViewSet(viewsets.ModelViewSet):
    """
    ViewSet for UserAudio objects.
    Provides both read and write operations for UserAudio models.

    For GET requests, it uses the UserAudioGetSerializer to serialize the response.
    For other requests (POST, PUT, PATCH, DELETE), it uses the UserAudioPostSerializer.

    The queryset is ordered by the timeStamp field.
    """
    queryset = UserAudio.objects.all().order_by('timeStamp')

    def get_serializer_class(self):
        """
        Returns the appropriate serializer class based on the request method.
        """
        if self.request.method == 'GET':
            return UserAudioGetSerializer
        return UserAudioPostSerializer  


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Solution objects.
    Provides read-only operations for Solution models. The client App will make a get request using id and timestamp.

    It uses the SolutionGetSerializer to serialize the response.

    The queryset is ordered by the timeStamp field.
    """
    queryset = UserAudio.objects.all().order_by('timeStamp')
    serializer_class = SolutionGetSerializer
