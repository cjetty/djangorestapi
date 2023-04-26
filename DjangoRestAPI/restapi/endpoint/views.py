from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .tests import EmployeeData

class EmployeeViewSet(APIView):
    def get(self, request):
        name = "Chandra"
        id = 200
        customdata = EmployeeData(name, id)
        serializer_class = EmployeeSerializer(customdata)
        return Response(status=status.HTTP_200_OK, data=serializer_class.data)