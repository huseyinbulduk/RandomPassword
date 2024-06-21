import tkinter as tk
from tkinter import messagebox
import random
import string

# Şifre oluşturma fonksiyonu
def generate_password():
    length = entry_length.get()
    if length.isdigit() and int(length) > 0:
        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(tk.END, password)
    else:
        messagebox.showwarning("Uyarı", "Geçerli bir uzunluk girin.")

# Ana pencere oluşturma
root = tk.Tk()
root.title("Random Password")

# Uzunluk girişi etiketi ve giriş alanı
label_length = tk.Label(root, text="Şifre Uzunluğu:", font=('Arial', 14))
label_length.pack(pady=5)

entry_length = tk.Entry(root, font=('Arial', 14))
entry_length.pack(pady=5)

# Şifre oluşturma butonu
button_generate = tk.Button(root, text="Şifre Oluştur", font=('Arial', 14), command=generate_password)
button_generate.pack(pady=5)

# Oluşturulan şifre için giriş alanı
label_password = tk.Label(root, text="Oluşturulan Şifre:", font=('Arial', 14))
label_password.pack(pady=5)

entry_password = tk.Entry(root, font=('Arial', 14))
entry_password.pack(pady=5)

# Pencereyi çalıştırma
root.mainloop()
