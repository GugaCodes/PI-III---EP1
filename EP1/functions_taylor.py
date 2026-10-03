from math import factorial, pi, sin

def calcular_coeficientes(N):
    coeficientes = [1.0]

    for n in range(1, N):
        soma = 0.0

        for k in range(1, n + 1):
            soma += (
                coeficientes[n - k]
                * (-1) ** k
                / factorial(2 * k)
            )

        coeficientes.append(-soma)

    return coeficientes


def taylor_cossecante(x, N):
    coeficientes = calcular_coeficientes(N)
    z = x - pi / 2
    resultado = 0.0

    for n in range(N):
        resultado += coeficientes[n] * z ** (2 * n)

    return resultado