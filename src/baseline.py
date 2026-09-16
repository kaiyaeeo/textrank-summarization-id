from typing import List


def ringkasan_awal_n(daftar_kalimat: List[str], n: int = 3) -> str:
    """
    Baseline sederhana: mengambil n kalimat pertama dari dokumen (Lead-N).

    Args:
        daftar_kalimat (List[str]): daftar kalimat dokumen.
        n (int): jumlah kalimat awal yang diambil.

    Returns:
        str: ringkasan naif hasil penggabungan n kalimat pertama.
    """
    return " ".join(daftar_kalimat[:n])
