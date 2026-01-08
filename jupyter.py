import pandas as pd
import numpy as np
from IPython.display import display  # Agar tidak warning di VS Code



try:
    df = pd.read_csv('calon_tni.csv')

    # Menstandarkan nama kolom agar sesuai
    df.columns = ['Nama', 'Alamat', 'Tinggi']
    df['Tinggi'] = pd.to_numeric(df['Tinggi'], errors='coerce')
    df.dropna(subset=['Tinggi'], inplace=True)
    df.reset_index(drop=True, inplace=True)

except FileNotFoundError:
    print("Error: File 'calon_tni.csv' tidak ditemukan. Menggunakan data contoh.")
    data = {
        'Nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka', 'Fajar', 'Gina', 'Galih', 'Hadi', 'Indah', 'Jilan',],
        'Alamat': [
            'Jl. Merdeka No. 10', 'Jl. Sudirman No. 5', 'Jl. Thamrin No. 20',
            'Jl. Gatot Subroto No. 15', 'Jl. Rasuna Said No. 8', 'Jl. Kuningan No. 12',
            'Jl. Cikini No. 3', 'Jl. Senayan No. 9', 'Jl. Kuningan No. 2',
        ],
        'Tinggi': [175, 178, 180, 180, 183, 185, 170, 168, 178, 160],
    }
    df = pd.DataFrame(data)

print("Data berhasil dimuat.\n")
print("=== Data Calon TNI ===\n")
display(df)

# Bagian 2: Statistik Dasar
print("=== Statistik Dasar Tinggi Badan ===")
print(df['Tinggi'].describe())

rata_rata = df['Tinggi'].mean()
median = df['Tinggi'].median()
maksimum = df['Tinggi'].max()
minimum = df['Tinggi'].min()

print(f"""
Rata-rata tinggi   : {rata_rata:.2f} cm
Tertinggi          : {maksimum} cm
Terendah           : {minimum} cm
Median             : {median:.2f} cm
""")

# Bagian 3: Pengelompokan Berdasarkan Rata-rata
rata_rata_tinggi = df['Tinggi'].mean()
df_tinggi_di_atas_rata = (
    df[df['Tinggi'] > rata_rata_tinggi]
    .sort_values(by='Nama', ascending=True)  # Urutkan nama dari A ke Z
    .reset_index(drop=True)
)

print("=== Calon di Atas Rata-rata Tinggi  ===")
display(df_tinggi_di_atas_rata[['Nama', 'Alamat', 'Tinggi']])

# Bagian 4: Urutan dari Tertinggi ke Terendah
df_urut_tinggi = df.sort_values(by='Tinggi', ascending=False).reset_index(drop=True)

print("=== Urutan Calon Berdasarkan Tinggi Badan (Tertinggi ke Terendah) ===")
display(df_urut_tinggi[['Nama', 'Alamat', 'Tinggi']])

# Bagian 4: Kategori Tinggi Badan
def kategori_tinggi(tinggi):
    if tinggi >= 180:
        return 'Tinggi'
    elif 170 <= tinggi <= 179:
        return 'Sedang'
    else:
        return 'Pendek'


df['Kategori'] = df['Tinggi'].apply(kategori_tinggi)

print("=== Daftar Calon dengan Kategori Tinggi Badan ===")
display(df[['Nama', 'Alamat', 'Tinggi', 'Kategori']])

# Bagian 5: Statistik Kategori
print("=== Jumlah Calon per Kategori ===")
print(df['Kategori'].value_counts().to_string())

#Statistik Lanjutan
standar_deviasi_sampel = df['Tinggi'].std(ddof=0)
variansi_sampel = df['Tinggi'].var(ddof=0)

print("\n=== Statistik Lanjutan ===")
print(f"Standar deviasi   : {round(standar_deviasi_sampel, 2)}")
print(f"Variansi          : {round(variansi_sampel, 2)}")

# Bagian 6: Calon Tertinggi
calon_tertinggi = df.loc[df['Tinggi'].idxmax()]

print("\n=== Calon dengan Tinggi Tertinggi ===")
print(f"Nama   : {calon_tertinggi['Nama']}")
print(f"Alamat : {calon_tertinggi['Alamat']}")
print(f"Tinggi : {int(calon_tertinggi['Tinggi'])} cm")

print("\nAnalisis data selesai.")