from rest_framework import serializers

from .models import UserAudio

class UserAudioPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAudio
        fields = ('id',
                  'timeStamp',
                  'createdAt',
                  'Audio_content',

    )

class UserAudioGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAudio
        fields = ('id',
                  'class_distribution',
                  'Video_content',
                  'Infant_cry_class_by_model',
                  'Infant_cry_class_rate',
                  'Infant_cry_class_by_user',)
        


class SolutionGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAudio
        fields = (
            'id',
            'timeStamp',
            'solution_audio',
            'text',
            'Video_content',
        )