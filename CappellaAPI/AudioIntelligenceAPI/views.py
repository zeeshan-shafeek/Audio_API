from django.shortcuts import render
from rest_framework import viewsets

from .serializer import UserAudioGetSerializer, UserAudioPostSerializer, SolutionGetSerializer
from .models import UserAudio


class UserAudioViewSet(viewsets.ModelViewSet):
    queryset = UserAudio.objects.all().order_by('timeStamp')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserAudioGetSerializer
        return UserAudioPostSerializer  


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserAudio.objects.all().order_by('timeStamp')
    serializer_class = SolutionGetSerializer
