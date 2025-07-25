from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("models/all-mpnet-base-v2")

def rank_sections_by_relevance(query, sections):
    query_vec = model.encode(query)
    scored = []

    for section in sections:
        sec_vec = model.encode(section["content"])
        sim = cosine_similarity([query_vec], [sec_vec])[0][0]
        scored.append((section, sim))

    return sorted(scored, key=lambda x: x[1], reverse=True)
