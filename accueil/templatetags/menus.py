from django import template
from blogApp.models import Category, Post
from django.db.models.functions import TruncMonth
register = template.Library()

@register.inclusion_tag('accueil/menus.html', takes_context=True)
def show_menus(context):
    user = context['user']
    cats = Category.objects.filter(post__status=2).distinct()

    archives = Post.objects.filter(status=2).order_by('-pub_date').annotate(month=TruncMonth('pub_date')).values('month').distinct()

    return {'user' : user, 'categories' : cats, 'archives': archives}


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()