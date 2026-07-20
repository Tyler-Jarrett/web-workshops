from django.shortcuts import render

from .models import Article, Section, Author

# Create your views here.
def list_news(request):
    news = Article.objects.all().order_by("-last_update_date", "-last_update_time")
    
    context = {
        'news': news
    }

    return render(request, 'news/list-news.html', context)

def detail_news(request, article_id):
    news = Article.objects.get(pk = article_id)
    
    context = {
        'news':news
    }

    return render(request, 'news/detail-news.html', context)