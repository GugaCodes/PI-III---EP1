import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from grafico_taylor import criar_grafico_taylor
from tabela_taylor import criar_tabela

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aproximação da Cossecante — Série de Taylor")
        self.geometry("1100x750")

        # Título
        ctk.CTkLabel(
            self,
            text="Gráficos da Cossecante",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(15,10))

        area_principal =ctk.CTkFrame(
            self,
            corner_radius=14,
        )
        area_principal.pack(fill="both", expand=True, padx=20, pady=(5,20))

        # Configuração da grade
        area_principal.grid_rowconfigure(0, weight=1)
        area_principal.grid_rowconfigure(1, weight=1)

        area_principal.grid_columnconfigure(0, weight=1)
        area_principal.grid_columnconfigure(1, weight=1)


        # Cria os graficos
        figura_aproximacao,figura_tempo, figura_erro = (
            criar_grafico_taylor()
        )

        # 1 - Aproximação
        quadro_aproximacao =ctk.CTkFrame(area_principal, corner_radius=12)
        quadro_aproximacao.grid(row=0, column=0, padx=(10,5), pady=(10,5),sticky="nsew")
        titulo_aproximacao = ctk.CTkLabel(quadro_aproximacao, text="Aproximação",font=ctk.CTkFont(size=20, weight="bold"))
        titulo_aproximacao.pack(pady=5)

        canvas_aproximacao = FigureCanvasTkAgg(figura_aproximacao, master=quadro_aproximacao)
        canvas_aproximacao.draw()
        canvas_aproximacao.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

        # 2 - Tempo
        quadro_tempo = ctk.CTkFrame(area_principal, corner_radius=12)
        quadro_tempo.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="nsew")
        titulo_tempo = ctk.CTkLabel(quadro_tempo, text = "Erro", font = ctk.CTkFont(size=20,weight="bold"))
        titulo_tempo.pack(pady=5)

        canvas_tempo = FigureCanvasTkAgg(figura_tempo, master=quadro_tempo)
        canvas_tempo.draw()
        canvas_tempo.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

        # 3 - Erro
        quadro_erro = ctk.CTkFrame(area_principal, corner_radius=12)
        quadro_erro.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky="nsew")
        titulo_erro = ctk.CTkLabel(quadro_erro, text = "Tempo de Execução", font = ctk.CTkFont(size=20,weight="bold"))
        titulo_erro.pack(pady=5)

        canvas_erro = FigureCanvasTkAgg(figura_erro, master=quadro_erro)
        canvas_erro.draw()
        canvas_erro.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

        # 4 - Tabela
        quadro_tabela = ctk.CTkFrame(area_principal,corner_radius=12)
        quadro_tabela.grid(row=1,column=1,padx=(5, 10),pady=(5, 10),sticky="nsew")
        titulo_tabela = ctk.CTkLabel(quadro_tabela,text="Tabela de Valores",font=ctk.CTkFont(size=20, weight="bold"))
        titulo_tabela.pack(pady=5)

        # Área da tabela
        area_tabela = ctk.CTkFrame(quadro_tabela,fg_color="transparent")

        area_tabela.pack(fill="both", expand=True,padx=10,pady=5)

        # Cabeçalho
        cabecalho = [
            "x(rad)",
            "csc(x)",
            "Taylor",
            "Erro"
        ]

        for coluna, texto in enumerate(cabecalho):
            label = ctk.CTkLabel(area_tabela,text=texto,font=ctk.CTkFont(size=14, weight="bold"))

            label.grid(row=0,column=coluna,padx=10,pady=5,sticky="ew")


        dados = criar_tabela()

        for linha, dados_linha in enumerate(dados, start=1):
            valores = dados_linha.split()

            for coluna, valor in enumerate(valores):
                label = ctk.CTkLabel(area_tabela,text=valor,font=ctk.CTkFont(size=13))

                label.grid(row=linha,column=coluna,padx=10,pady=3,sticky="ew")


        for coluna in range(4):
            area_tabela.grid_columnconfigure(
                coluna,
                weight=1
            )
# Execução
if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()
