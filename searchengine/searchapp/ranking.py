# searchapp/ranking.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def bow_ranking(query, pages):
    """
    Bag-of-words ranking algorithm.
    """
    # Combine titles and content into a single text for each page
    documents = [f"{page.title}" for page in pages]
    
    # Debugging: Print the documents for inspection
    print("Documents:", documents)

    # Add the query as an additional document
    documents.append(query)

    # Convert to bag-of-words matrix
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(documents)

    # Check if bow_matrix is empty
    if bow_matrix.shape[0] == 0:
        return []  # or raise an appropriate exception

    # Check if there are sufficient samples for comparison
    if bow_matrix.shape[0] < 2:
        return []  # or raise an appropriate exception

    # Calculate cosine similarity between the query and each document
    cosine_similarities = cosine_similarity(bow_matrix[-1], bow_matrix[:-1]).flatten()

    # Sort results based on similarity scores
    results = [(page, score) for page, score in zip(pages, cosine_similarities)]
    results.sort(key=lambda x: x[1], reverse=True)

    return results
