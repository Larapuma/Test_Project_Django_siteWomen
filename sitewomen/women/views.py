from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import AddPostForm
from .models import Women, Category, TagPost

menu =[{'title':'О сайте','url_name':'about'},
{'title':'Добавить статью','url_name':'addpage'},
{'title':'Обратная связь','url_name':'contact'},
{'title':'Войти','url_name':'login'},
]


def index(request: HttpRequest):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    #эквивалентные строчки
    posts = Women.published.all().select_related('cat')
    data = {'title':"Главная страница",
            'menu':menu,
            "posts":posts,
            'cat_selected': 0,
            }
    return render(request,'women/index.html',context = data)

def about(request: HttpRequest):

    return render(request,'women/about.html',{'title':"О сайте","menu":menu})

def login(request):
    return HttpResponse("Авторизация")


def contact(request):
    return HttpResponse("Обратная связь")


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()

    data = {'menu':menu,
            'title':"Добавление статьи",
            'form':form,
    }
    return render(request,'women/addpage.html', data)





def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



def categories(request: HttpRequest, cat_id: int):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id:{cat_id}</p>")
# Create your views here.
def categories_by_slug(request: HttpRequest, cat_slug: str):
    if request.POST: print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug:{cat_slug}</p>")


def archive(request, year):
    if year>2025:
        uri = reverse('cats',args=('music',))
        return redirect('cats',"music")#адрес главной страницы
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


def show_category(request, cat_slug):

    category = get_object_or_404(Category,slug = cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {'title': f"Рубрика:{category.name}",
            'menu': menu,
            "posts": posts,
            'cat_selected': category.pk,
            }
    return render(request,'women/index.html',context= data)


def show_tag_postlist(request,tag_slug):
    tag = get_object_or_404(TagPost,slug = tag_slug)
    posts = tag.tags.filter(is_published = Women.Status.PUBLISHED).select_related('cat')

    data={'title': f"Тег:{tag.tag}",
            'menu': menu,
            "posts": posts,
            'cat_selected': None,
            }
    return  render(request,'women/index.html',context=data)