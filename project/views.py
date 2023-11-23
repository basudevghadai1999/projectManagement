from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer

from .models import Project
# Create your views here.

@api_view(['GET'])
def projectOverview(request):
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
def projectList(request):
	project = Project.objects.all().order_by('-id')
	serializer = ProjectSerializer(project, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request, pk):
	project = Project.objects.get(id=pk)
	serializer = ProjectSerializer(project, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def projectCreate(request):
	serializer = ProjectSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def projectUpdate(request, pk):
	project = Project.objects.get(id=pk)
	serializer = ProjectSerializer(instance=project, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def projectDelete(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()

	return Response('Item succsesfully delete!')




