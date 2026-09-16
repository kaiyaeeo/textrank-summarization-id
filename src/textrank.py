import networkx as nx
from typing import List
from src.representation import bangun_matriks_kemiripan


def textrank_ringkas(daftar_kalimat: List[str], jumlah_kalimat_ringkasan: int = 3) -> str:
    """
    Meringkas daftar kalimat menggunakan algoritma TextRank (berbasis PageRank).

    Args:
        daftar_kalimat (List[str]): daftar kalimat dari satu dokumen.
        jumlah_kalimat_ringkasan (int): jumlah kalimat yang diambil untuk ringkasan.

    Returns:
        str: ringkasan hasil gabungan kalimat-kalimat terpilih, sesuai urutan asli.
    """
    if len(daftar_kalimat) == 0:
        return ""
    if len(daftar_kalimat) <= jumlah_kalimat_ringkasan:
        return " ".join(daftar_kalimat)

    matriks_kemiripan = bangun_matriks_kemiripan(daftar_kalimat)
    graf = nx.from_numpy_array(matriks_kemiripan)
    skor_kalimat = nx.pagerank(graf)

    urutan_peringkat = sorted(
        ((skor_kalimat[i], i) for i in range(len(daftar_kalimat))),
        reverse=True
    )
    indeks_terpilih = sorted([indeks for _, indeks in urutan_peringkat[:jumlah_kalimat_ringkasan]])
    ringkasan = " ".join([daftar_kalimat[i] for i in indeks_terpilih])
    return ringkasan