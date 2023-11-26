# searchapp/search.py

from searchapp.models import CrawledPage
from django.db.models import Q

def search(query):
    # Perform a case-insensitive search in title and content fields
    results = CrawledPage.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return results
