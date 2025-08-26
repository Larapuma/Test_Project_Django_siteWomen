from django.db import models

from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0,'Черновик' #Черновик
        PUBLISHED = 1, 'Опубликовано' # Опубликовано
    title = models.CharField(max_length=255)#поле типа Varchar в таблице women
    slug = models.SlugField(max_length=255,unique= True,db_index = True)
    content = models.TextField(blank=True)#Позволяет не заносить туда что-то с самого начала, чтобы можно было добавить и сразу и потом
    time_create = models.DateTimeField(auto_now_add=True)#Автоматически заполняет это поле в момент добавления этой записи(заполняет датой занесения)
    time_update = models.DateTimeField(auto_now=True)#Это поле меняется каждое новое обновление
    is_published = models.BooleanField(choices=Status.choices,default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField("TagPost",blank=True, related_name='tags')


    objects = models.Manager()
    published = PublishedManager()




    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post',kwargs={"post_slug":self.slug})


    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs = {"cat_slug":self.slug})

class TagPost(models.Model):
    tag = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tag",kwargs = {'tag_slug':self.slug})