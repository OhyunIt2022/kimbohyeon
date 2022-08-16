from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='글 제목', max_length=20)
    context =models.TextField(verbose_name= '글 내용')
    
    created_at = models.DateTimeField(verbose_name='생성시간', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정시간', auto_now=True)
    

