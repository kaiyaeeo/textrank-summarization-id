# Peringkasan Dokumen Otomatis Berbahasa Indonesia dengan TextRank

Sistem extractive summarization untuk artikel berita Bahasa Indonesia menggunakan algoritma TextRank (adaptasi PageRank).

## Instalasi
```bash
git clone https://github.com/username/textrank-summarization-id.git
cd textrank-summarization-id
pip install -r requirements.txt
```

## Cara Menjalankan
```python
from src.summarizer import summarize_document

teks = "Tempel artikel berita di sini..."
ringkasan = summarize_document(teks, top_n=3)
print(ringkasan)
```

## Menjalankan Testing
```bash
pytest tests/
```

## Menjalankan Evaluasi Penuh
Buka dan jalankan `notebooks/05_evaluation_test.ipynb` secara berurutan setelah `01` sampai `04`.

## Dataset
[IndoSum](https://huggingface.co/datasets/SEACrowd/indosum) — 14.083 data train, 1.880 validation, 2.810 test.
