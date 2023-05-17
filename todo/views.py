# from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer


class TodosAPIView(APIView):
  def get(self, request): #전체 조회 뷰는 get 방식으로 요청 처리
    todos = Todo.objects.filter(complete=False) #complete이 false인 todo들을 필터링하도록 한다
    serializer = TodoSimpleSerializer(todos, many=True) #이후 시리얼라이저를 통과시켜 보낼 수 있는 형태로 변환
    return Response(serializer.data, status=status.HTTP_200_OK) #response 객체 형태로 전달하는 과정

  def post(self, request):
    serializer = TodoCreateSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class TodoAPIView(APIView):
  def get(self,request,pk):
    todo = get_object_or_404(Todo,id=pk)
    serializer = TodoDetailSerializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)

    # todo = get_object_or_404(Todo, id=pk) 코드는 Todo 모델에서 id 필드의 값이 pk와 일치하는 객체를 가져오는데,
    #  해당 객체가 존재하지 않는 경우 404 에러 페이지를 반환합니다. 반환된 객체는 todo 변수에 할당됩니다.

  def put(self, request, pk): #수정 기능
    todo = get_object_or_404(Todo, id = pk)
    serializer = TodoCreateSerializer(todo, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DoneTodosAPIView(APIView): #완료 투두 목록 조회용 
  def get(self, request):
    dones = Todo.objects.filter(complete = True)
    serializer = TodoSimpleSerializer(dones, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
  def get(self, request, pk):
    done = get_object_or_404(Todo, id = pk)
    done.complete = True
    done.save()
    serializer = TodoDetailSerializer(done)
    return Response(status=status.HTTP_200_OK)