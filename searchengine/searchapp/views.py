

from django.shortcuts import render

# Create your views here.
from .models import CrawledPage
from .ranking import bow_ranking
from .search import search
from .server import index
from PIL import Image
from .features import Features
import numpy as np 
from pathlib import Path
from datetime import datetime




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



def image_search(request):
    
    fea = Features()
    feature = []
    img_paths = []
    for feature_path in Path("searchapp/static/feature").glob("*.npy"):
        feature.append(np.load(feature_path))
        img_paths.append(Path("random_images") / (feature_path.stem + ".jpg"))
    feature = np.array(feature)
    
    if request.method == "POST":
        file = request.FILES["query_img"]
         
        img = Image.open(file)
        
        query = fea.extract(img)
        dists = np.linalg.norm(feature - query, axis=1)
        ids = np.argsort(dists)[:5]
        scores = [(dists[id], img_paths[id]) for id in ids] 
        context = {'scores': scores}
        
        return render(request, "searchapp/index.html", context)
    else:
        return render(request, "searchapp/index.html")