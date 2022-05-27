from django.shortcuts import render
from .models import Article
# Create your views here.

def get_data(request):
    #return render(request, 'test.html', {'name': 'Ravi'})
    articles = Article.objects.all().order_by('date')
    return render(request, 'test.html', {'articles': articles})




