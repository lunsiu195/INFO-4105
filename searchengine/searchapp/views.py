from django.shortcuts import render

# Create your views here.
from .models import CrawledPage
from .ranking import bow_ranking
from .search import search

def home(request):
    print("Home view is being called!")
    return render(request, 'searchapp/home.html')

def search_view(request):
    query = request.GET.get('q', '')
    print(f"Query: {query}") 
    pages = CrawledPage.objects.all()
    results = bow_ranking(query, pages)
    print("Results:", results) 
    context = {'query': query, 'results': results}
    return render(request, 'searchapp/search_results.html', context)