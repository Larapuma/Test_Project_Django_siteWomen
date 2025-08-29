from django import template
from django.db.models import Count

import women.views as veiws
from women.models import Category, TagPost

register = template.Library()

# #Самый простой тег(самая простая реализация)
# @register.simple_tag(name='getcats')
# def get_categories():
#     return veiws.cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"cats":cats, "cat_selected":cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}