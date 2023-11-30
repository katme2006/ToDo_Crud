from django.urls import path, register_converter

from .views import All_lists

url = [
    path('',All_lists.as_view(), name = "all_lists")
     path('<int:id>/',a_lists.as_view(), name = "all_lists")
]