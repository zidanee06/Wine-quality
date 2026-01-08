from tkinter import *
from tkinter import ttk
root=Tk()
root.title("App Biodata Diri")

Luser=ttk.Label(root, text= "NAMA").grid(row=0, column=0, pady=10,)
Enama=ttk.Entry(root).grid(row=0, column=1, pady=15)
Lalamat=ttk.Label(root, text= "ALAMAT").grid(row=1, column=0, pady=10)
Enama=ttk.Entry(root).grid(row=1, column=1, pady=15)
Lno=ttk.Label(root, text= "NO TELPON").grid(row=2, column=0, pady=10)
Eno=ttk.Entry(root).grid(row=2, column=1, pady=15)
Lusia=ttk.Label(root, text= "USIA").grid(row=3,column=0, pady=10)
Eusia=ttk.Entry(root).grid(row=3, column=1, pady=10)
Lkrj=ttk.Label(root, text= "PEKERJAAN").grid(row=4, column=0, pady=10)
Ekrj=ttk.Entry(root).grid(row=4, column=1, pady=15)

root.mainloop()