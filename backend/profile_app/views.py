from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import ProfileSerializer
from .models import Profile as ProfileModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ProfileAPIView(APIView):
    def get(self,request):
        articles=ProfileModel.objects.all()
        serializer=ProfileSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)        
    def post(self,request):
        serializer=ProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)