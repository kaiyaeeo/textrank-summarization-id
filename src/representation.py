import numpy as np
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def bangun_matriks_kemiripan(daftar_kalimat: List[str]) -> np.ndarray:
    """
    Membangun matriks kemiripan antar-kalimat menggunakan TF-IDF dan cosine similarity.

    Args:
        daftar_kalimat (List[str]): daftar kalimat dari satu dokumen.

    Returns:
        np.ndarray: matriks kemiripan berukuran (jumlah_kalimat x jumlah_kalimat).
    """
    jumlah_kalimat = len(daftar_kalimat)
    if jumlah_kalimat < 2:
        return np.zeros((jumlah_kalimat, jumlah_kalimat))

    vectorizer = TfidfVectorizer()
    matriks_tfidf = vectorizer.fit_transform(daftar_kalimat)
    matriks_kemiripan = cosine_similarity(matriks_tfidf)
    np.fill_diagonal(matriks_kemiripan, 0)  # kalimat tidak dibandingkan dengan dirinya sendiri
    return matriks_kemiripan