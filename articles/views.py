from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment


def index(request):
    latest_list = Article.objects.order_by('-date')[:5]
    return render(request, 'articles/list.html', {"latest_list": latest_list})


def detail(request, pk):
    try:
        a = Article.objects.get(id=pk)
    except:
        raise Http404("No articles")

    return render(request, 'articles/detail.html', {'article': a})
