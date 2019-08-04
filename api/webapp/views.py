from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees,user_auth
from . serializers import employeesSerializer


class employeesList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many = True)
        return Response(serializer.data)

    def post(self,request):
        employees2 = employees.objects.all()
        serializer = employeesSerializer(employees2, many = True)
        return Response(serializer.data)

# class Login(APIView):
#
#     def post(self, request):
#         username = request.data.get("usrname", "")
#         password = request.data.get("password","")

class Signup(APIView):

    def post(self, request):
        username = request.data.get("usrname", "")
        password = request.data.get("password","")


        if  username  and  password:
            user_auth(
                user_name=username,
                password=password,

                ).save()
            return Response(
            data={
            "message": "User successfully added to database."
            },
            status=status.HTTP_201_CREATED)
        return Response(
            data={
                "error": "Both username and password  required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
