from src.preprocessing import pisahkan_kalimat
from src.textrank import textrank_ringkas


def ringkas_dokumen(teks: str, jumlah_kalimat_ringkasan: int = 3) -> str:
    """
    Fungsi utama: menerima teks dokumen mentah, mengembalikan ringkasan.

    Args:
        teks (str): teks dokumen mentah (belum diproses).
        jumlah_kalimat_ringkasan (int): jumlah kalimat pada ringkasan akhir.

    Returns:
        str: ringkasan dokumen.

    Contoh:
        >>> ringkas_dokumen("Kalimat satu. Kalimat dua. Kalimat tiga. Kalimat empat.", 2)
        'Kalimat satu. Kalimat tiga.'
    """
    daftar_kalimat = pisahkan_kalimat(teks)
    return textrank_ringkas(daftar_kalimat, jumlah_kalimat_ringkasan)