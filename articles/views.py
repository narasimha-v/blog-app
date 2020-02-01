from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})


@login_required
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article-list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
