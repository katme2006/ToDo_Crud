from django.db import models

# Create your models here.
from django.db import models

class Task_List(models.Model):
    list_name = models.CharField(max_length=100)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    parent_list = models.ForeignKey(Task_List, on_delete=models.CASCADE)

class SubTask(models.Model):
    sub_task_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
