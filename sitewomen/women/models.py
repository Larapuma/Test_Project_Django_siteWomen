from django.db import models

from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)#поле типа Varchar в таблице women
    content = models.TextField(blank=True)#Позволяет не заносить туда что-то с самого начала, чтобы можно было добавить и сразу и потом
    time_create = models.DateTimeField(auto_now_add=True)#Автоматически заполняет это поле в момент добавления этой записи(заполняет датой занесения)
    time_update = models.DateTimeField(auto_now=True)#Это поле меняется каждое новое обновление
    is_published = models.BooleanField(default=True)