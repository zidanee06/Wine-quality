import tkinter as tk
from tkinter import messagebox
from collections import deque

# Inisialisasi antrian restoran
antrian = deque()

# Fungsi untuk menambahkan pelanggan ke antrian
def tambah_antrian():
    nama = entry_nama.get()
    if nama:
        antrian.append(nama)
        update_listbox()
        entry_nama.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Kosong", "Silakan masukkan nama pelanggan.")

# Fungsi untuk melayani pelanggan
def layani_antrian():
    if antrian:
        nama = antrian.popleft()
        update_listbox()
        messagebox.showinfo("Sedang Melayani", f"Pesanan untuk {nama} sedang disiapkan.")
    else:
        messagebox.showinfo("Antrian Kosong", "Tidak ada pelanggan dalam antrian.")

# Fungsi untuk memperbarui tampilan antrian
def update_listbox():
    listbox_antrian.delete(0, tk.END)
    for i, nama in enumerate(antrian, start=1):
        listbox_antrian.insert(tk.END, f"{i}. {nama}")

# GUI setup
root = tk.Tk()
root.title("Sistem Antrian Restoran")
root.geometry("400x350")

# Label dan entry input
label_nama = tk.Label(root, text="Nama Pelanggan:")
label_nama.pack(pady=5)

entry_nama = tk.Entry(root, width=30)
entry_nama.pack(pady=5)

# Tombol tambah dan layani
btn_tambah = tk.Button(root, text="Tambah ke Antrian", command=tambah_antrian)
btn_tambah.pack(pady=5)

btn_layani = tk.Button(root, text="Layani Pelanggan", command=layani_antrian)
btn_layani.pack(pady=5)

# Label dan listbox antrian
label_antrian = tk.Label(root, text="Daftar Antrian:")
label_antrian.pack(pady=5)

listbox_antrian = tk.Listbox(root, width=40, height=10)
listbox_antrian.pack(pady=5)

# Jalankan aplikasi
root.mainloop()

