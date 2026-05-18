from django.shortcuts import render
from students.models import Attendance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ResultInfoSerializer, StudentInfoSerializer
from .models import Result
from students.models import StudentInfo

# Create your views here.
@api_view()
def student_attendance(request, student_class, student_id):
    try:
        Attendance.objects.create_attendance(student_class, student_id)
        return Response({"Status": "Atendance Counted Successfully"}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"Status": "Attendance already has taken"}, status=status.HTTP_400_BAD_REQUEST)


# Class Based View (CBV)
class StudentAttendance(APIView):
    def get(self, request, student_class, student_id):
        try:
            Attendance.objects.create_attendance(student_class, student_id)
            return Response({"Status": "Atendance Counted Successfully"}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Status": "Attendance already has taken"}, status=status.HTTP_400_BAD_REQUEST)


class ResultInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        result_serializer = ResultInfoSerializer(data=request.data)
        if result_serializer.is_valid():
            board = result_serializer.validated_data["board"]
            roll = result_serializer.validated_data["roll"]
            result_obj = Result.objects.get(board=board, roll=roll)
            return Response({"Result": result_obj.gpa})

        return Response(result_serializer.errors)


class CreateStudentInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        create_student_serializer = StudentInfoSerializer(data=request.data)
        if create_student_serializer.is_valid():
            create_student_serializer.save()
            return Response({"Status": "Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"Status": create_student_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


