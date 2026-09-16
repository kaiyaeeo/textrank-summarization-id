import re
import nltk
from typing import List

nltk.donwload('punkt')
from nltk.tokenize import sent_tokenize

def bersihkan_teks(teks: str) -> str:
    """
    Membersihkan teks mentah dari spasi berlebih dan karakter tidak relevan.

    Args:
        teks (str): teks mentah yang akan dibersihkan.
        
    Returns:
        str: teks yang sudah bersih dan rapi.
    """
    
    if not isinstance(teks, str) or teks.strip() == "":
        return ""
    teks = re.sub(r'\s+', ' ', teks)
    teks = re.sub(r'[^\w\s.,!?]', '', teks)
    return teks.strip()

def pisahkan_kalimat(teks: str) -> List[str]:
    """
    Memecah sebuah dokumen menjadi daftar kalimat.

    Args:
        teks (str): teks dokumen yang akan dipecah
        
    Returns:
        List[str]: daftar kalimat hasil tokenisasi, tanpa kalimat kosong.
    """
    teks_bersih = bersihkan_teks(teks)
    if teks_bersih == "":
        return []
    daftar_kalimat = sent_tokenize(teks_bersih)
    return [kalimat for kalimat in daftar_kalimat if len(kalimat.strip()) > 0]