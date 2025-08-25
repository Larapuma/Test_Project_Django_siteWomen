from django.urls import path, re_path, register_converter
from . import views,convertors
register_converter(convertors.FourDigitYearConverter,"year4")
urlpatterns = [
    #ПИСАТЬ КОВЕРТОРЫ НУЖНО В ПОРЯДКЕ УБЫВАНИЯ ЖЁТСКОСТИ ТИПИЗАЦИИ, ТО ЕСТЬ
    #ЕСЛИ ПОМЕНЯТЬ INT И SLUG, ТО ЕСТЬ СНАЧАЛА SLUG, ПОТОМ INT, ТОГДА ДО INT НИЧЕГО НЕ БУДЕТ ДОХОДИТЬ
    path('',views.index, name='home' ),#http://127.0.0.1:8000
    path('about/',views.about, name = "about"),
    path('addpage/',views.addpage,name='addpage'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path("post/<int:post_id>/",views.show_post, name = "post"),
    path('category/<int:cat_id>/',views.show_category,name = "category")
    # path('cats/<int:cat_id>/',views.categories, name = "cats_id"),#http://127.0.0.1:8000/целое_число/
    # path('cats/<slug:cat_slug>/',views.categories_by_slug, name = 'cats'),#http://127.0.0.1:8000/произвольные лат. символы/
    # path('archive/<year4:year>/', views.archive,name = 'archive')
]