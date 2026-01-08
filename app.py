import tkinter as tk 
from tkinter import messagebox 
 
def submit_form(): 
    nama = entry_nama.get() 
    email = entry_email.get() 
    umur = entry_umur.get() 
 
    if not nama or not email or not umur: 
        messagebox.showerror("Input Error", "Semua field harus diisi!") 
        return 
 
    label_output.config(text=f"Nama: {nama}\nEmail: {email}\nUmur: {umur}") 
 
root = tk.Tk() 
root.title("Form Sederhana") 
root.geometry("300x200") 
 
label_nama = tk.Label(root, text="Nama:") 
label_nama.pack(pady=5) 
entry_nama = tk.Entry(root) 
entry_nama.pack(pady=5) 
 
label_email = tk.Label(root, text="Email:") 
label_email.pack(pady=5) 
entry_email = tk.Entry(root) 
entry_email.pack(pady=5) 
 
label_umur = tk.Label(root, text="Umur:") 
label_umur.pack(pady=5) 
entry_umur = tk.Entry(root) 
entry_umur.pack(pady=5) 
 
submit_button = tk.Button(root, text="Submit", command=submit_form) 
submit_button.pack(pady=10) 
 
label_output = tk.Label(root, text="") 
label_output.pack(pady=5) 
 
root.mainloop()
