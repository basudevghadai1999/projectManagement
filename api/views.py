from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Task
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
	permission_classes = [IsAuthenticated]
	api_urls = {
		         'http://localhost:8000/project/projects/',

                  'http://localhost:8000/project/project-list/',

                   'http://localhost:8000/project/project-detail/<str:pk>/',

                    'http://localhost:8000/project/project-create/',

                    'http://localhost:8000/project/project-update/<str:pk>/',

                    'http://localhost:8000/project/project-delete/<str:pk>/',

                    ####################################  USER #########################

                    'http://localhost:8000/user/users/',

                    'http://localhost:8000/user/user-list/',

                    'http://localhost:8000/user/user-detail/<str:pk>/',

                    'http://localhost:8000/user/user-create/',

                    'http://localhost:8000/user/user-update/<str:pk>/',

                    'http://localhost:8000/user/user-delete/<str:pk>/',

                    ############################ Task ###############################

                    'http://localhost:8000/task/tasks/',

                    'http://localhost:8000/task/task-list/',

                    'http://localhost:8000/task/task-detail/<str:pk>/',

                    'http://localhost:8000/task/task-create/',

                    'http://localhost:8000/task/task-update/<str:pk>/',

                    'http://localhost:8000/task/task-delete/<str:pk>/'
				}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskLists(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



