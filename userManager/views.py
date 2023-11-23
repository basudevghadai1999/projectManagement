from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from .models import usermanager
# Create your views here.

@api_view(['GET'])
def userOverview(request):
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
def userList(request):
	tasks = usermanager.objects.all().order_by('-id')
	serializer = UserSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
	tasks = usermanager.objects.get(id=pk)
	serializer = UserSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)




@api_view(['POST'])
def userUpdate(request, pk):
	task = usermanager.objects.get(id=pk)
	serializer = UserSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	task = usermanager.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')





