from django import template
import aset.views as views
from aset.models import Category

register = template.Library()

@register.inclusion_tag('aset/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}