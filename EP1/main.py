import customtkinter as ctk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from grafico_taylor import criar_grafico_taylor

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aproximação da Cossecante — Série de Taylor")
        self.geometry("1000x700")

        # Painel principal
        frame = ctk.CTkFrame(self, corner_radius=14)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        ctk.CTkLabel(
            frame,
            text="Gráfico da Aproximação da Cossecante",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=10)

        # Área do gráfico
        area_grafico = tk.Canvas(frame, highlightthickness=0)
        area_grafico.pack(fill="both", expand=True, padx=10, pady=10)

        # Importa e desenha o gráfico
        figura = criar_grafico_taylor()
        canvas = FigureCanvasTkAgg(figura, master=area_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

# Execução
if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()
