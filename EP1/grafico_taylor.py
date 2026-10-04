import timeit
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


    enes = [1, 2, 3, 4, 5, 6, 7, 8]

    erros = []
    tempos = []

    for n in enes:
        soma_erros = 0
        inicio = timeit.default_timer()

        for x in x_valores:
            valor_taylor = taylor_cossecante(x, n)
            valor_real = 1 / sin(x)

            erro = abs(valor_taylor - valor_real)
            soma_erros += erro

        fim = timeit.default_timer()

        erro_medio = soma_erros / len(x_valores)
        tempo = fim - inicio

        erros.append(erro_medio)
        tempos.append(tempo)


    # Criação da figura

    figura_aproximacao = plt.figure(figsize=(5, 3.5))
    ax1 = figura_aproximacao.add_subplot(111)

    ax1.plot(x_valores, y_real, label="Função real", color="black", linewidth=2)
    ax1.plot(x_valores, y_N2, label="Taylor N=2", linestyle="--", color="red")
    ax1.plot(x_valores, y_N4, label="Taylor N=4", linestyle="--", color="blue")
    ax1.plot(x_valores, y_N8, label="Taylor N=8", linestyle="--", color="green")

    ax1.set_xlabel("x (rad)")
    ax1.set_ylabel("csc(x)")
    ax1.set_title("Aproximação da cossecante pela Série de Taylor")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Limites bem definidos
    ax1.set_xlim(min(x_valores), max(x_valores))
    ax1.set_ylim(min(y_real) * 0.9, max(y_real) * 1.1)

    figura_aproximacao.tight_layout()

    #Grafico erro X N

    figura_erro = plt.figure(figsize=(5, 3.5))
    ax2 = figura_erro.add_subplot(111)

    ax2.plot(enes, erros,marker="o")
    ax2.set_xlabel("N")
    ax2.set_ylabel("Erro médio")
    ax2.set_title("Erro da Série de Taylor")
    ax2.grid(alpha=0.3)

    figura_erro.tight_layout()

    #Grafico do tempo
    figura_tempo = plt.figure(figsize=(5, 3.5))
    ax3 = figura_tempo.add_subplot(111)

    ax3.plot(enes, tempos,marker="o")
    ax3.set_xlabel("N")
    ax3.set_ylabel("Tempo de execução (s)")
    ax3.set_title("Tempo de execução x N")
    ax3.grid(alpha=0.3)

    figura_tempo.tight_layout()

    return figura_aproximacao, figura_erro, figura_tempo
