from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from apiapp.serializers import UserSerializer,ClientsSerializer,ProjectsSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from apiapp.models import clients,projects

# Create your views here.

# client entity data operations
@csrf_exempt
def client(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        serializer = ClientsSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors,status=400)
    else:
        Emps = clients.objects.all()
        ser = ClientsSerializer(Emps,many=True)
        return JsonResponse(ser.data,status=200,safe=False)
    
@csrf_exempt
def clientAct(request, clientid):
    client = clients.objects.get(id = clientid)
    if client:
        if request.method == "GET":
            serialiser = ClientsSerializer(client)
            data = serialiser.data
            return JsonResponse(data,status=200)
        elif request.method == "DELETE":
            client.delete()
            success = {'success':'client is deleted !!!'}
            return JsonResponse(success,status = 204)
        elif request.method == "PUT":
            data = JSONParser().parse(request)
            data['id'] = clientid
            data['id'] = int(data['id'])
            serializer = ClientsSerializer(client,data = data) 
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
    else:
        error = {'error':'Invalid Client id, Firstly check your Client id'}
        return JsonResponse(error,status=404)
    

# project entity data operations

@csrf_exempt
def project(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        serializer = ProjectsSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors,status=400)
    else:
        Emps = projects.objects.all()
        ser = ProjectsSerializer(Emps,many=True)
        return JsonResponse(ser.data,status=200,safe=False)


@csrf_exempt
def projectAct(request, pid):
    proj = projects.objects.get(id = pid)
    if client:
        if request.method == "GET":
            serialiser = ProjectsSerializer(proj)
            data = serialiser.data
            return JsonResponse(data,status=200)
        elif request.method == "DELETE":
            proj.delete()
            success = {'success':'project is deleted !!!'}
            return JsonResponse(success,status = 204)
        elif request.method == "PUT":
            data = JSONParser().parse(request)
            data['id'] = pid
            data['id'] = int(data['id'])
            serializer = ProjectsSerializer(proj,data = data) 
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
    else:
        error = {'error':'Invalid proj id, Sorry but this project does not exist'}
        return JsonResponse(error,status=404)
    



# user entity data ops
@csrf_exempt
def usersinfo(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return JsonResponse(serializer.errors,status=400)
    else:
        Emps = User.objects.all()
        ser = UserSerializer(Emps,many=True)
        return JsonResponse(ser.data,status=200,safe=False)
    
@csrf_exempt
def userAct(request, uid):
    user = User.objects.get(id = uid)
    if user:
        if request.method == "GET":
            serialiser = UserSerializer(user)
            data = serialiser.data
            return JsonResponse(data,status=200)
        elif request.method == "DELETE":
            user.delete()
            success = {'success':'User is deleted !!!'}
            return JsonResponse(success,status = 204)
        elif request.method == "PUT":
            data = JSONParser().parse(request)
            data['id'] = uid
            data['id'] = int(data['id'])
            serializer = UserSerializer(user,data = data) 
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
    else:
        error = {'error':'Invalid user id, User not found'}
        return JsonResponse(error,status=404)
    