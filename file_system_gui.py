import os
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb

class FileSystemSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulasi Sistem File")
        self.root.geometry("800x600")
        
        self.style = tb.Style("cosmo")
        self.setup_ui()

    def setup_ui(self):
        # Frame untuk pengelolaan direktori
        dir_frame = ttk.LabelFrame(self.root, text="Pengelolaan Direktori")
        dir_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(dir_frame, text="Nama Direktori:").grid(row=0, column=0, padx=5, pady=5)
        self.dir_name = ttk.Entry(dir_frame)
        self.dir_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(dir_frame, text="Buat Direktori", command=self.create_directory).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(dir_frame, text="Hapus Direktori", command=self.delete_directory).grid(row=0, column=3, padx=5, pady=5)

        # Area untuk simulasi alokasi file
        file_frame = ttk.LabelFrame(self.root, text="Simulasi Alokasi File")
        file_frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(file_frame, text="Pilih Metode Alokasi:").grid(row=0, column=0, padx=5, pady=5)
        self.allocation_method = ttk.Combobox(file_frame, values=["Contiguous", "Linked", "Indexed"], state="readonly")
        self.allocation_method.grid(row=0, column=1, padx=5, pady=5)
        self.allocation_method.set("Contiguous")

        ttk.Button(file_frame, text="Simulasikan", command=self.simulate_allocation).grid(row=0, column=2, padx=5, pady=5)

        self.output = tk.Text(file_frame, height=20)
        self.output.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def create_directory(self):
        dir_name = self.dir_name.get()
        if dir_name:
            try:
                os.makedirs(dir_name)
                messagebox.showinfo("Sukses", f"Direktori '{dir_name}' berhasil dibuat.")
            except FileExistsError:
                messagebox.showerror("Error", f"Direktori '{dir_name}' sudah ada.")
        else:
            messagebox.showwarning("Peringatan", "Nama direktori tidak boleh kosong!")

    def delete_directory(self):
        dir_name = self.dir_name.get()
        if dir_name:
            try:
                os.rmdir(dir_name)
                messagebox.showinfo("Sukses", f"Direktori '{dir_name}' berhasil dihapus.")
            except FileNotFoundError:
                messagebox.showerror("Error", f"Direktori '{dir_name}' tidak ditemukan.")
            except OSError:
                messagebox.showerror("Error", f"Direktori '{dir_name}' tidak kosong.")
        else:
            messagebox.showwarning("Peringatan", "Nama direktori tidak boleh kosong!")

    def simulate_allocation(self):
        method = self.allocation_method.get()
        if method == "Contiguous":
            self.simulate_contiguous_allocation()
        elif method == "Linked":
            self.simulate_linked_allocation()
        elif method == "Indexed":
            self.simulate_indexed_allocation()
        else:
            self.output.insert("end", "Metode alokasi tidak valid.\n")

    def simulate_contiguous_allocation(self):
        self.output.insert("end", "Simulasi alokasi contiguous:\n")
        self.output.insert("end", "Blok-blok file disimpan secara berurutan.\n")

    def simulate_linked_allocation(self):
        self.output.insert("end", "Simulasi alokasi linked:\n")
        self.output.insert("end", "Setiap blok file memiliki pointer ke blok berikutnya.\n")

    def simulate_indexed_allocation(self):
        self.output.insert("end", "Simulasi alokasi indexed:\n")
        self.output.insert("end", "Sebuah blok indeks menunjuk ke semua blok file.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemSimulator(root)
    root.mainloop()
