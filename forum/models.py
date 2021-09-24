from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Forum(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fo_title = models.CharField('제목', max_length=200)
    fo_desc = models.TextField('내용')
    fo_day = models.DateField('등록일', default=timezone.now)

    class Meta:
        verbose_name_plural = "게시판"
    
    def __str__(self):
        return self.fo_title