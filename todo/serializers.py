from rest_framework import serializers
from .models import Todo

# 전체 조회용 시리얼라이저 -> 제목, 완료여부, 중요 여부 필요 

class TodoSimpleSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Todo
    fields = ('id','title','complete','important')

    # 시리얼라이저 -> 데이터를 원하는 형태로 보내고 받기 위한 일종의 양식
    # 보내는 데이터 형식에 따라 시리얼라이저가 필요
    
class TodoDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id','title','description','created','complete','important')

class TodoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('title','description','important')