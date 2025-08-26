from django.db import models

from django.db import models
from django.urls import reverse

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_published=1)

class Women(models.Model):
    title = models.CharField(max_length=255)#поле типа Varchar в таблице women
    slug = models.SlugField(max_length=255,unique= True,db_index = True)
    content = models.TextField(blank=True)#Позволяет не заносить туда что-то с самого начала, чтобы можно было добавить и сразу и потом
    time_create = models.DateTimeField(auto_now_add=True)#Автоматически заполняет это поле в момент добавления этой записи(заполняет датой занесения)
    time_update = models.DateTimeField(auto_now=True)#Это поле меняется каждое новое обновление
    is_published = models.BooleanField(default=True)




    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post',kwargs={"post_slug":self.slug})

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
