# Aproximação da Cossecante — Série de Taylor

## Integrantes

- Gustavo Silva Oliveira
- Yasmin Aparecida
- Leticia Santana

---

## Tema

Aproximação da função cossecante utilizando a Série de Taylor.

O projeto consiste no desenvolvimento de um programa em Python capaz de apresentar uma aproximação da função cossecante por meio da Série de Taylor, permitindo analisar os resultados através de gráficos e de uma tabela de valores.

A função estudada no projeto é:

**y = csc(x)**

ou:

**csc(x) = 1 / sen(x)**

---

## Objetivo

O objetivo principal do projeto é aplicar os conceitos matemáticos de Séries de Taylor por meio de uma implementação computacional da função cossecante.

O programa foi desenvolvido para apresentar visualmente os resultados obtidos, permitindo analisar:

- A aproximação da função pela Série de Taylor;
- O tempo de execução dos cálculos;
- O erro da aproximação;
- Os valores da função e da aproximação em uma tabela.

Além da implementação matemática, o projeto possui uma interface gráfica para organizar e facilitar a visualização dos resultados.

---

## Sobre a Série de Taylor

A Série de Taylor é uma forma de representar uma função por meio de uma soma de termos, utilizando as derivadas da função calculadas em torno de um determinado ponto.

A forma geral da Série de Taylor pode ser representada por:

**f(x) = f(a) + f'(a)(x - a) + [f''(a) / 2!] (x - a)² + [f'''(a) / 3!] (x - a)³ + ...**

De forma resumida:

**f(x) = Σ [f⁽ⁿ⁾(a) / n!] · (x - a)ⁿ**

onde:

- **f(x)** é a função que será aproximada;
- **a** é o ponto em torno do qual a série é desenvolvida;
- **f⁽ⁿ⁾(a)** representa a derivada de ordem n calculada em a;
- **n!** representa o fatorial de n.

Neste projeto, a função estudada é:

**f(x) = csc(x)**

Como:

**csc(x) = 1 / sen(x)**

a função não é definida quando:

**sen(x) = 0**

Isso ocorre nos pontos:

**x = kπ, onde k ∈ ℤ**

Esses pontos devem ser considerados durante os cálculos e na representação gráfica.

---

## Funcionamento do programa

O programa possui uma interface gráfica desenvolvida utilizando a biblioteca **CustomTkinter**.

Ao executar o programa, uma janela é aberta apresentando quatro áreas principais:

1. **Aproximação**
2. **Tempo de Execução**
3. **Erro**
4. **Tabela de Valores**

Os gráficos são gerados utilizando a biblioteca **Matplotlib** e incorporados diretamente à interface gráfica.

A tabela apresenta os valores utilizados para comparar a função cossecante com a aproximação obtida pela Série de Taylor.

---

## Interface do programa

A interface possui uma organização em formato de grade, dividida em duas linhas e duas colunas.

A disposição dos elementos é:

| Posição | Conteúdo |
|---|---|
| Superior esquerdo | Gráfico da Aproximação |
| Superior direito | Gráfico do Tempo de Execução |
| Inferior esquerdo | Gráfico do Erro |
| Inferior direito | Tabela de Valores |

A aplicação utiliza o modo escuro e um tema azul.

---

## Gráficos

### 1. Gráfico de Aproximação

O gráfico de aproximação apresenta a comparação entre a função cossecante e o resultado obtido através da Série de Taylor.

Através desse gráfico, é possível observar o comportamento da aproximação em relação à função original.

---

### 2. Gráfico de Tempo de Execução

O gráfico de tempo de execução apresenta o tempo necessário para realizar os cálculos utilizados na aproximação.

Esse gráfico permite analisar o desempenho computacional do método utilizado.

---

### 3. Gráfico de Erro

O gráfico de erro apresenta a diferença entre os valores da função cossecante e os valores obtidos pela aproximação da Série de Taylor.

O erro pode ser representado por:

**Erro = |f(x) - f_Taylor(x)|**

onde:

- **f(x)** representa o valor da função cossecante;
- **f_Taylor(x)** representa o valor aproximado pela Série de Taylor.

A análise do erro permite verificar a precisão da aproximação.

---

## Tabela de valores

O programa apresenta uma tabela contendo quatro colunas:

| Coluna | Descrição |
|---|---|
| `x(rad)` | Valor de x em radianos |
| `csc(x)` | Valor da função cossecante |
| `Taylor` | Valor obtido pela aproximação de Taylor |
| `Erro` | Diferença entre o valor real e o valor aproximado |

A tabela permite comparar numericamente os resultados obtidos.

Exemplo da estrutura da tabela:

```text
x(rad)    csc(x)    Taylor    Erro
------------------------------------
valor     valor     valor     valor
valor     valor     valor     valor
valor     valor     valor     valor
