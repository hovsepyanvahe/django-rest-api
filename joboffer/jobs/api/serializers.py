from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        exclude = ('id',)

    def validate(self, data):
        """ Check that description and title are different """
        if data['job_title'] == data['job_description']:
            raise serializers.ValidationError('Title and Description must be different')
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError('Title has to be at least 30 characters long')
        return value

