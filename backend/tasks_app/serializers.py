# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Task_List, Task, SubTask # import Pokemon model from models.py

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List # specify what model this serializer is for
        fields = ['id', 'list_name'] 

    # DUNDER METHOD
    def __str__(self):
        return f"{self.id} - {self.list_name}"
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # specify what model this serializer is for
        fields = ['id', 'task_name', 'completed', 'parent_list'] 


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask # specify what model this serializer is for
        fields = ['id', 'sub_task_name', 'completed', 'parent_task'] 


