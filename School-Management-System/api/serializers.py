from rest_framework import serializers
from students.models import StudentShiftInfo

class ResultInfoSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=12)
    roll = serializers.IntegerField()


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentShiftInfo
        fields = '__all__'