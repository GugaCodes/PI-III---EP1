import matplotlib.pyplot as plt
from math import pi, sin
from functions_taylor import taylor_cossecante

def criar_grafico_taylor():
    # Valores de x
    x_valores = [i * 0.01 for i in range(1, 315)]

    # Função real
    y_real = [1 / sin(x) for x in x_valores]

    # Aproximações de Taylor
    y_N2 = [taylor_cossecante(x, 2) for x in x_valores]
    y_N4 = [taylor_cossecante(x, 4) for x in x_valores]
    y_N8 = [taylor_cossecante(x, 8) for x in x_valores]

    # Criação da figura
    figura, ax = plt.subplots(figsize=(8,5))
    ax.plot(x_valores, y_real, label="Função real", color="black", linewidth=2)
    ax.plot(x_valores, y_N2, label="Taylor N=2", linestyle="--", color="red")
    ax.plot(x_valores, y_N4, label="Taylor N=4", linestyle="--", color="blue")
    ax.plot(x_valores, y_N8, label="Taylor N=8", linestyle="--", color="green")

    ax.set_xlabel("x (rad)")
    ax.set_ylabel("csc(x)")
    ax.set_title("Aproximação da cossecante pela Série de Taylor")
    ax.legend()
    ax.grid(alpha=0.3)

    # Limites bem definidos
    ax.set_xlim(min(x_valores), max(x_valores))
    ax.set_ylim(min(y_real) * 0.9, max(y_real) * 1.1)

    figura.tight_layout()
    return figura
