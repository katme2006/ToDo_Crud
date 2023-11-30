from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response  # Used for returning API responses
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST  # Import HTTP status codes
from rest_framework.status import HTTP_201_CREATED

from .models import Task_List, Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer, ListSerializer


# Create your views here.

class All_lists(APIView):

    def get(self,request):
        lists= ListSerializer(Task_List.objects.order_by('id', many=True))
        return Response(lists.data)
    

class A_list(APIView):

    def get(self, request):
        a_list = get_object_or_404(Task_List, id=id)
        return Response(ListSerializer(a_list).data)
    
    