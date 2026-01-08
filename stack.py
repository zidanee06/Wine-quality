import tkinter as tk
from tkinter import messagebox
import random

class HanoiNaturalStack:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower of Hanoi - Stack Natural")

        self.canvas = tk.Canvas(root, width=600, height=300, bg='white')
        self.canvas.pack()

        self.num_disks = 4
        self.stacks = [[], [], []]
        self.selected_from = None

        self.create_random_disks()
        self.draw_towers()

        button_frame = tk.Frame(root)
        button_frame.pack()
        for i in range(3):
            btn = tk.Button(button_frame, text=f"Tiang {i+1}", command=lambda i=i: self.handle_click(i), width=10)
            btn.grid(row=0, column=i, padx=10, pady=10)

    def create_random_disks(self):
        all_disks = list(range(self.num_disks, 0, -1))  # [4,3,2,1]
        random.shuffle(all_disks)
        for disk in all_disks:
            peg = random.randint(0, 2)
            self.stacks[peg].insert(0, disk)  # dimasukkan dari bawah

    def handle_click(self, peg_index):
        if self.selected_from is None:
            if not self.stacks[peg_index]:
                messagebox.showinfo("Info", "Tiang ini kosong.")
                return
            self.selected_from = peg_index
        else:
            if self.move_disk(self.selected_from, peg_index):
                self.selected_from = None
                self.draw_towers()
                if self.check_win():
                    messagebox.showinfo("Menang!", "Semua cakram berhasil disusun di Tiang 3!")
            else:
                messagebox.showwarning("Tidak valid", "Tidak bisa meletakkan cakram besar di atas yang kecil.")
                self.selected_from = None

    def move_disk(self, from_peg, to_peg):
        if not self.stacks[from_peg]:
            return False
        moving_disk = self.stacks[from_peg][-1]  # ambil yang paling atas
        if self.stacks[to_peg] and self.stacks[to_peg][-1] < moving_disk:
            return False
        self.stacks[from_peg].pop()
        self.stacks[to_peg].append(moving_disk)  # taruh di atas
        return True

    def draw_towers(self):
        self.canvas.delete("all")
        peg_x = [100, 300, 500]

        # Gambar tiang
        for x in peg_x:
            self.canvas.create_rectangle(x - 5, 100, x + 5, 280, fill='gray')

        # Gambar cakram per stack
        for peg_index, stack in enumerate(self.stacks):
            for i, disk_size in enumerate(stack):  # index 0 = bawah
                width = 20 + disk_size * 20
                x_center = peg_x[peg_index]
                y = 280 - i * 20
                self.canvas.create_rectangle(x_center - width//2, y, x_center + width//2, y - 15, fill='skyblue')
                self.canvas.create_text(x_center, y - 8, text=str(disk_size), font=('Arial', 10))

        # Petunjuk tujuan
        self.canvas.create_text(500, 50, text=">> Susun besar ke kecil di sini!", fill="darkgreen", font=('Arial', 12, 'bold'))

    def check_win(self):
        return (
            len(self.stacks[2]) == self.num_disks and
            self.stacks[2] == list(range(self.num_disks, 0, -1))  # [4,3,2,1]
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = HanoiNaturalStack(root)
    root.mainloop()