from django.urls import path
from . import views
from .views import ArticleMonthArchiveView

app_name = 'blogApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('draft/', views.draft, name='Brouillon'),
    path('<int:post_id>/', views.post, name='Post'),
    path('category/<int:category_id>/', views.category, name='Category'),
    path('<int:year>/<int:month>/',
         ArticleMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    path('edit/<int:pk>/', views.editPost, name='editPost'),
]
