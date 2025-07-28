from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("local_models/all-MiniLM-L12-v2")

def rank_sections_by_relevance(query, sections):
    query_vec = model.encode([query])[0]  # batch of 1
    section_texts = [sec["content"] for sec in sections]
    section_vecs = model.encode(section_texts, batch_size=16, show_progress_bar=False) 
    sims = cosine_similarity([query_vec], section_vecs)[0]
    scored = list(zip(sections, sims))
    return sorted(scored, key=lambda x: x[1], reverse=True)