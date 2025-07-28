# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-mpnet-base-v2')
# model.save('.models/all-mpnet-base-v2')  # Save model to local folder
# print("Model downloaded and saved offline.")

from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L12-v2')
# model.save('.models/all-MiniLM-L12-v2')  # Save model to local folder
# print("Model downloaded and saved offline.")

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")
model.save("local_models/all-MiniLM-L12-v2")
