import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# File CSV hasil cleaning dari notebook.
folder = Path(__file__).resolve().parent

@st.cache_data
def baca_data():
    harian = pd.read_csv(folder / "main_data.csv", parse_dates=["tanggal"])
    per_jam = pd.read_csv(folder / "hour_data.csv", parse_dates=["tanggal"])
    return harian, per_jam

harian, per_jam = baca_data()

st.title("Dashboard Penyewaan Sepeda")
st.write("Analisis penyewaan sepeda pada periode 2011–2012.")

pilihan_tahun = st.sidebar.selectbox("Pilih tahun", ["Semua Tahun", "2011", "2012"])
st.sidebar.caption("Data Bike Sharing, 2011–2012")

if pilihan_tahun != "Semua Tahun":
    tahun = int(pilihan_tahun)
    harian = harian[harian["tanggal"].dt.year == tahun].copy()
    per_jam = per_jam[per_jam["tanggal"].dt.year == tahun].copy()

warna_biasa = "#9cb8c8"
warna_tertinggi = "#177245"
warna_terendah = "#d97735"

def format_angka(nilai, desimal=0):
    return f"{nilai:,.{desimal}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def warna_batang(data):
    nilai_max = data.max()
    nilai_min = data.min()
    return [warna_tertinggi if x == nilai_max else warna_terendah if x == nilai_min else warna_biasa for x in data]

st.subheader("Ringkasan Data")
total = int(harian["jumlah_penyewaan"].sum())
rata_harian = harian["jumlah_penyewaan"].mean()
jam_rata = per_jam.groupby("jam")["jumlah_penyewaan"].mean()
puncak_jam = int(jam_rata.idxmax())

kol1, kol2, kol3 = st.columns(3)
kol1.metric("Total penyewaan", format_angka(total))
kol2.metric("Rata-rata per hari", format_angka(rata_harian, 1))
kol3.metric("Jam paling ramai", f"{puncak_jam:02d}.00")

st.caption("Hijau = tertinggi, oranye = terendah, biru muda = data lainnya.")

# Pertanyaan 1: jam dengan rata-rata penyewaan tertinggi.
st.subheader("1. Rata-rata Penyewaan Berdasarkan Jam")
rata_jam = per_jam.groupby("jam")["jumlah_penyewaan"].mean().reindex(range(24))
fig, ax = plt.subplots(figsize=(11, 4))
ax.bar(rata_jam.index, rata_jam.values, color=warna_batang(rata_jam))
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata penyewaan")
ax.set_xticks(range(24))
ax.spines[["top", "right"]].set_visible(False)
st.pyplot(fig)
plt.close(fig)
st.write(f"Jam tersibuk: **{rata_jam.idxmax():02d}.00**, rata-rata **{format_angka(rata_jam.max(), 2)}** penyewaan. Jam paling sepi: **{rata_jam.idxmin():02d}.00**.")

# Pertanyaan 2: hari kerja dibandingkan hari nonkerja.
st.subheader("2. Perbandingan Hari Kerja dan Hari Nonkerja")
rata_hari = harian.groupby("hari_kerja")["jumlah_penyewaan"].mean().reindex([0, 1])
nama_hari = ["Hari Nonkerja", "Hari Kerja"]
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(nama_hari, rata_hari.values, color=warna_batang(rata_hari))
ax.set_ylabel("Rata-rata penyewaan per hari")
ax.spines[["top", "right"]].set_visible(False)
st.pyplot(fig)
plt.close(fig)
selisih = abs(rata_hari.loc[1] - rata_hari.loc[0])
lebih_tinggi = "hari kerja" if rata_hari.loc[1] > rata_hari.loc[0] else "hari nonkerja"
st.write(f"Rata-rata pada **{lebih_tinggi}** lebih tinggi dengan selisih **{format_angka(selisih, 2)}** penyewaan per hari.")

# Pertanyaan 3: total setiap bulan, ditandai titik tertinggi dan terendah.
st.subheader("3. Total Penyewaan per Bulan")
bulanan = harian.groupby(harian["tanggal"].dt.to_period("M"))["jumlah_penyewaan"].sum()
bulanan.index = bulanan.index.astype(str)
fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(range(len(bulanan)), bulanan.values, color="#66889c", marker="o", linewidth=1.8)
idx_tertinggi = int(bulanan.values.argmax())
idx_terendah = int(bulanan.values.argmin())
ax.scatter(idx_tertinggi, bulanan.iloc[idx_tertinggi], color=warna_tertinggi, s=80, zorder=5)
ax.scatter(idx_terendah, bulanan.iloc[idx_terendah], color=warna_terendah, s=80, zorder=5)
ax.set_xticks(range(len(bulanan)))
ax.set_xticklabels(bulanan.index, rotation=60, ha="right")
ax.set_ylabel("Total penyewaan")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)
st.write(f"Bulan tertinggi: **{bulanan.idxmax()}** ({format_angka(bulanan.max())} penyewaan). Bulan terendah: **{bulanan.idxmin()}** ({format_angka(bulanan.min())} penyewaan).")

# Pertanyaan 4: rata-rata penyewaan berdasarkan kondisi cuaca.
st.subheader("4. Rata-rata Penyewaan Berdasarkan Cuaca")
nama_cuaca = {1: "Cerah / Sedikit Berawan", 2: "Berkabut / Berawan", 3: "Salju / Hujan Ringan", 4: "Hujan Lebat / Hujan Es"}
rata_cuaca = harian.groupby("kondisi_cuaca")["jumlah_penyewaan"].mean().sort_index()
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar([nama_cuaca.get(i, str(i)) for i in rata_cuaca.index], rata_cuaca.values, color=warna_batang(rata_cuaca))
ax.set_ylabel("Rata-rata penyewaan per hari")
ax.tick_params(axis="x", labelrotation=12)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)
st.write(f"Cuaca dengan rata-rata tertinggi: **{nama_cuaca.get(int(rata_cuaca.idxmax()))}** ({format_angka(rata_cuaca.max(), 2)} penyewaan per hari).")

st.subheader("Kesimpulan Singkat")
st.write("Penyewaan sepeda dipengaruhi pola waktu penggunaan dan kondisi cuaca. Ketersediaan sepeda dapat diprioritaskan pada jam sibuk, serta disesuaikan dengan hari dan musim permintaan tinggi.")
st.caption("Sumber: Bike Sharing Dataset (data tahun 2011–2012).")

