from django import template
import women.views as veiws

register = template.Library()

#Самый простой тег(самая простая реализация)
@register.simple_tag(name='getcats')
def get_categories():
    return veiws.cats_db

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = veiws.cats_db
    return {"cats":cats, "cat_selected":cat_selected}