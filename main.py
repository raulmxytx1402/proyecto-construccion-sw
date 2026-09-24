import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivinanza:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Juego de Adivinanza")
        self.root.geometry("350x250")
        
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.max_intentos = 7

        tk.Label(root, text="Adivina el número (1 - 100)", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.lbl_info = tk.Label(root, text=f"Tienes {self.max_intentos} intentos restantes.", font=("Arial", 10))
        self.lbl_info.pack(pady=5)

        self.txt_numero = tk.Entry(root, font=("Arial", 12), justify="center")
        self.txt_numero.pack(pady=10)

        self.btn_adivinar = tk.Button(root, text="Adivinar", command=self.comprobar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_adivinar.pack(pady=10)

    def comprobar(self):
        try:
            intento = int(self.txt_numero.get())
            self.intentos += 1
            restantes = self.max_intentos - self.intentos

            if intento < self.numero_secreto:
                messagebox.showinfo("Pista", "➡️ El número secreto es MAYOR")
            elif intento > self.numero_secreto:
                messagebox.showinfo("Pista", "⬅️ El número secreto es MENOR")
            else:
                messagebox.showinfo("🎉 ¡Ganaste!", f"¡Felicidades! Adivinaste en {self.intentos} intentos.")
                self.root.destroy()
                return

            if restantes == 0:
                messagebox.showerror("💀 Fin del juego", f"Sin intentos restantes. El número era {self.numero_secreto}.")
                self.root.destroy()
            else:
                self.lbl_info.config(text=f"Intentos restantes: {restantes}")
                self.txt_numero.delete(0, tk.END)

        except ValueError:
            messagebox.showwarning("Atención", "Ingresa un número entero válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinanza(root)
    root.mainloop()