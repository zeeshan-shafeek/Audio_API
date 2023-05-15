from rest_framework import serializers

from .models import UserAudio

class UserAudioPostSerializer(serializers.HyperlinkedModelSerializer):
    
    """
    Serializer for creating UserAudio objects through POST requests.
    The data from the client app will be retrieved using this endpoint.
    """

    class Meta:
        model = UserAudio
        fields = ('id',
                  'timeStamp',
                  'createdAt',
                  'Audio_content',

    )

class UserAudioGetSerializer(serializers.HyperlinkedModelSerializer):
    
    """
    Serializer for retrieving UserAudio objects through GET requests.
    The client app will use this endpoint to get information regarding each recording.
    """

    class Meta:
        model = UserAudio
        fields = ('id',
                  'class_distribution',
                  'Video_content',
                  'Infant_cry_class_by_model',
                  'Infant_cry_class_rate',
                  'Infant_cry_class_by_user',)
        

class SolutionGetSerializer(serializers.HyperlinkedModelSerializer):

    """
    Serializer for retrieving Solution objects through GET requests.
    The client app will get data from the solution API using this endpoint.
    """

    class Meta:
        model = UserAudio
        fields = (
            'id',
            'timeStamp',
            'solution_audio',
            'text',
            'Video_content',
        )