from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False)
  important = models.BooleanField(default=False)


# 파이썬 클래스 내의 __str__ 메소드를 정의하는 코드
  def __str__(self):  
    return self.title

    # __str__ 메소드는 객체를 문자열로 표현할 때 사용됩니다. self는 메소드가 호출되는 해당 객체를 나타냅니다.

# 이 코드에서는 title 필드를 문자열로 반환합니다. title 필드는 클래스 내에서 정의된 필드 중 하나일 것입니다.

# 따라서, 이 코드는 해당 클래스의 객체를 문자열로 표현할 때, 객체의 title 필드 값을 반환하게 됩니다.