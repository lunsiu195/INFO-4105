from index import *
import requests
from requests.exceptions import RequestException
import pandas as pd 
from data_storage import DBConnec
from urllib.parse import quote_plus

def search(query, pages=int(RESULTS/10)):
    results = []
    for i in range(0, pages):
        start = i * 10 + i
        url = SEARCH_URL.format(key=SEARCH_KEY, cx=SEARCH_ID, query=quote_plus(query), start=start)
        response = requests.get(url)
        data = response.json()
        results += data["items"]
    res_df = pd.DataFrame.from_dict(results)
    res_df["rank"] = list(range(1, res_df.shape[0] + 1))
    res_df = res_df[["link", "rank", "title"]]
    return res_df