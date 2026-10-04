import math
from functions_taylor import taylor_cossecante

def criar_tabela():

    valores = {
        math.pi / 6: 2,
        math.pi / 4: math.sqrt(2),
        math.pi / 3: 2/ math.sqrt(3),
        math.pi / 2: 1,
        2 * math.pi / 3:2 / math.sqrt(3),
        3 * math.pi / 4: math.sqrt(2),
        5 * math.pi / 6: 2
    }

    dados = []

    for x, valor_real in valores.items():

        valor_taylor = taylor_cossecante(x, 8)
        erro = abs (valor_real - valor_taylor)

        dados.append(
            f"{x:.4f}     "
            f"{valor_real:.6f}     "
            f"{valor_taylor:.6f}     "
            f"{erro:.6f}"
        )

    return dados
