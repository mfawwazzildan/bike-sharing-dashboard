# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda menggunakan **Bike Sharing Dataset** pada periode 2011–2012.

Analisis dilakukan untuk mengetahui pola penyewaan sepeda berdasarkan jam, hari kerja, bulan, dan kondisi cuaca. Hasil analisis kemudian divisualisasikan melalui dashboard interaktif menggunakan Streamlit.

## Pertanyaan Bisnis

1. Bagaimana pola rata-rata penyewaan sepeda berdasarkan jam?
2. Bagaimana perbandingan penyewaan sepeda pada hari kerja dan hari nonkerja?
3. Bagaimana tren jumlah penyewaan sepeda setiap bulan?
4. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?

## Struktur Folder

```text
Bike-Sharing-Dashboard/
├── Dashboard/
│   ├── Dashboard.py
│   ├── main_data.csv
│   └── hour_data.csv
├── day.csv
├── hour.csv
├── README.md
└── requirements.txt
```

## Cara Menjalankan Dashboard Secara Lokal

**1. Clone repository**

**2. Masuk ke folder proyek**

**3. Instal library yang dibutuhkan**

**4. Jalankan dashboard Streamlit**

```bash
python -m streamlit run Dashboard/Dashboard.py
```

**5. Buka dashboard**

Setelah berhasil dijalankan, buka alamat berikut melalui browser:

http://localhost:8501

## Dashboard Online

Dashboard dapat diakses secara online melalui Streamlit Community Cloud.

**Link Dashboard:** wait


## Fitur Dashboard

- Filter data berdasarkan tahun.
- Menampilkan total penyewaan sepeda.
- Menampilkan rata-rata penyewaan harian.
- Menampilkan jam penyewaan tersibuk.
- Visualisasi penyewaan berdasarkan jam.
- Perbandingan penyewaan hari kerja dan nonkerja.
- Analisis tren penyewaan bulanan.
- Analisis berdasarkan kondisi cuaca.
- Highlight warna untuk menunjukkan nilai tertinggi dan terendah.

## Dataset

Dataset yang digunakan adalah Bike Sharing Dataset dengan periode 2011–2012.


## Library yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
pribadi.
