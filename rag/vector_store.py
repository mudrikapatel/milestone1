import os
import pickle
import faiss
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class BugVectorStore:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.index = None
        self.data = None

    def build(self, csv_file="bug_dataset.csv"):
        # Read dataset
        self.data = pd.read_csv(csv_file)

        # Combine useful fields into one searchable document
        documents = (
            self.data["Title"].fillna("") + " " +
            self.data["Description"].fillna("") + " " +
            self.data["Root_Cause"].fillna("") + " " +
            self.data["Suggested_Fix"].fillna("")
        )

        # TF-IDF embeddings
        vectors = self.vectorizer.fit_transform(documents)

        embeddings = vectors.astype(np.float32).toarray()

        # Build FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        # Save everything
        os.makedirs("faiss_index", exist_ok=True)

        faiss.write_index(
            self.index,
            "faiss_index/bug.index"
        )

        with open(
            "faiss_index/vectorizer.pkl",
            "wb"
        ) as f:
            pickle.dump(self.vectorizer, f)

        self.data.to_pickle(
            "faiss_index/bug_data.pkl"
        )

        print("✅ FAISS Index Created Successfully")