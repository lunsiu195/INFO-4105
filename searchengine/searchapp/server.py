import numpy as np
from PIL import Image
from .features import Features
from datetime import datetime
from pathlib import Path
from django import template
from django.shortcuts import render
from django.http import HttpRequest

register = template.Library()


fea = Features()
feature = []
img_paths = []
for feature_path in Path("static/feature").glob("*.npy"):
    feature.append(np.load(feature_path))
    img_paths.append(Path("static/random_images") / (feature_path.stem + ".jpg"))
feature = np.array(feature)

request = HttpRequest()
def index():
    if request.method == "POST":
        file = request.files["query_img"]
         
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        
        query = fea.extract(img)
        dists = np.linalg.norm(feature - query, axis=1)
        ids = np.argsort(dists)[:20]
        scores = [(dists[id], img_paths[id]) for id in ids] 
        
        return render(request, "index.html", query_path = uploaded_img_path, scores = scores)
    else:
        return render(request, "index.html")

