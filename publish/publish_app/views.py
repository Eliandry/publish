from django.shortcuts import render, get_object_or_404
from .models import Term, News, Article, HistoricalEvent

def home(request):
    terms = Term.objects.all()[:5]
    news = News.objects.order_by('-created_at')[:5]
    articles = Article.objects.order_by('-created_at')[:5]
    historical_events = HistoricalEvent.objects.order_by('-date')[:5]

    context = {
        'terms': terms,
        'news': news,
        'articles': articles,
        'historical_events': historical_events,
    }
    return render(request, 'main.html', context)

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news_item})


def article_list(request):
    news = Article.objects.all()
    return render(request, 'article_list.html', {'news': news})

def article_detail(request, pk):
    news_item = get_object_or_404(Article, pk=pk)
    return render(request, 'news_detail.html', {'news': news_item})

def terms_list(request):
    terms = Term.objects.all()
    return render(request, 'terms.html', {'terms': terms})

def history_list(request):
    news = HistoricalEvent.objects.all()
    return render(request, 'history_list.html', {'news': news})

def history_detail(request,pk):
    news_item = get_object_or_404(HistoricalEvent, pk=pk)
    return render(request, 'history_detail.html', {'news': news_item})