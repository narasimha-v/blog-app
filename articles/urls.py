from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('',views.articles,name='article-list'),
    path('create',views.article_create,name='article-create'),
    path('<slug>',views.article_details, name='details')
]