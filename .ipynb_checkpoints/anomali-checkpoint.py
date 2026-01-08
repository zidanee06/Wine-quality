import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Tambahkan import matplotlib untuk memastikan visualisasi berjalan jika diinstal

# 1. Muat Data
# Pastikan nama file adalah 'titanic.csv' dan berada di direktori yang sama
file_path = 'titanic.csv'
df = pd.read_csv(file_path)

# 2. Pembersihan Data Awal (BAGIAN YANG DIPERBAIKI)
# Untuk menghilangkan FutureWarning, kita tidak lagi menggunakan inplace=True pada chain assignment.
# Kita melakukan assignment (penugasan) hasilnya kembali ke kolom 'fare'.
df['fare'] = df['fare'].fillna(df['fare'].median())

# 3. Deteksi Anomali menggunakan Metode IQR
# IQR (Interquartile Range) adalah selisih antara kuartil ketiga (Q3) dan kuartil pertama (Q1).
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1

# Hitung Batas Atas dan Batas Bawah
# Batas Atas/Bawah = Q3/Q1 +/- 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 4. Identifikasi dan Tampilkan Anomali
anomalies = df[(df['fare'] < lower_bound) | (df['fare'] > upper_bound)]

# 5. Tampilkan Hasil Analisis
print("--- Hasil Analisis Anomali (Outlier) pada Kolom 'Fare' ---")
print(f"Kuartil Pertama (Q1): {Q1:.2f}")
print(f"Kuartil Ketiga (Q3): {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Batas Bawah Anomali: {lower_bound:.2f}")
print(f"Batas Atas Anomali: {upper_bound:.2f}")
print("-" * 50)
print(f"Total Baris Data: {len(df)}")
print(f"Jumlah Anomali yang Ditemukan: {len(anomalies)}")
print("-" * 50)

# Tampilkan 10 Anomali dengan Tarif Termahal
print("\n10 Anomali (Outlier) dengan 'Fare' Termahal:")
print(anomalies.sort_values(by='fare', ascending=False).head(10)[['name', 'pclass', 'fare']])

# 6. Visualisasi (Opsional)
try:
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['fare'], vert=False)
    plt.title('Box Plot of Fare (Tarif Tiket)')
    plt.xlabel('Fare')
    
    # Menandai Batas Atas dan Bawah pada plot
    plt.axvline(upper_bound, color='r', linestyle='--', label='Batas Atas')
    plt.axvline(lower_bound, color='b', linestyle='--', label='Batas Bawah')
    plt.legend()
    plt.show()
except ImportError:
    print("\nVisualisasi tidak ditampilkan. Install matplotlib (pip install matplotlib) untuk melihat Box Plot.")