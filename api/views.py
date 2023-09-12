from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

# Create your views here.


class PersonDetail(APIView):
    def get(self, request):
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if Person.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This person already exists')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class PersonInfo(APIView):
    def get(self, request, id):
        try:
            obj = Person.objects.get(id=id)

        except Person.DoesNotExist:
            msg = {"msg": "Not Found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Person.objects.get(id=id)

        except Person.DoesNotExist:
            msg = {"msg": "Not Found Error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer =PersonSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            obj = Person.objects.get(id=id)

        except Person.DoesNotExist:
            msg = {"msg": "Not Found Error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            msg = {"msg": "Not Found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    


