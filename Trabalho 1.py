import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def naive_multiplication(vec1, vec2):
    '''
    Realiza a multiplicação ingênua entre dois vetores representando números grandes.

    Descrição:
        Este método realiza a multiplicação direta de cada elemento do primeiro vetor
        com cada elemento do segundo vetor. Os resultados parciais são acumulados em
        uma estrutura de dados para compor o resultado final. O algoritmo possui
        complexidade temporal O(n^2), sendo adequado para pequenos tamanhos de entrada.

    Parâmetros:
        vec1 (list): Primeiro vetor de inteiros, representando o primeiro número grande.
        vec2 (list): Segundo vetor de inteiros, representando o segundo número grande.

    Retorno:
        list: Vetor de inteiros representando o resultado da multiplicação.
    '''
    n = len(vec1)
    result = [0] * (2 * n)
    for i in range(n):
        for j in range(n):
            result[i + j] += vec1[i] * vec2[j]
    return result

def karatsuba(vec1, vec2):
    '''
    Implementa o algoritmo de Karatsuba para multiplicação eficiente de dois vetores
    representando números grandes.

    Descrição:
        O algoritmo de Karatsuba divide o problema de multiplicação em partes menores
        utilizando uma abordagem recursiva. Ele reduz o número de multiplicações
        necessárias ao usar combinações de somas e diferenças dos elementos dos vetores,
        resultando em uma complexidade temporal de O(n^log2(3)).

    Parâmetros:
        vec1 (list): Primeiro vetor de inteiros, representando o primeiro número grande.
        vec2 (list): Segundo vetor de inteiros, representando o segundo número grande.

    Retorno:
        list: Vetor de inteiros representando o resultado da multiplicação.
    '''
    n = len(vec1)
    if n == 1:
        return [vec1[0] * vec2[0]]

    mid = n // 2

    # Divide os vetores em partes baixa e alta
    low1, high1 = vec1[:mid], vec1[mid:]
    low2, high2 = vec2[:mid], vec2[mid:]

    # Calcula resultados parciais
    z0 = karatsuba(low1, low2)
    z1 = karatsuba([low1[i] + high1[i] for i in range(mid)], [low2[i] + high2[i] for i in range(mid)])
    z2 = karatsuba(high1, high2)

    # Combina os resultados parciais no resultado final
    result = [0] * (2 * n)
    for i in range(len(z0)):
        result[i] += z0[i]
    for i in range(len(z1)):
        result[mid + i] += z1[i] - z0[i] - z2[i]
    for i in range(len(z2)):
        result[2 * mid + i] += z2[i]

    return result

k = random.randint(100, 200)
sizes = np.linspace(10, 10000, k, dtype=int)
m = random.randint(10, 20)

'''
Variáveis principais:

- k: Número de diferentes tamanhos de entrada a serem testados. Escolhido aleatoriamente no intervalo [100, 200].
     Define o número de pontos no gráfico, representando tamanhos de entrada distintos.

- sizes: Vetor contendo os tamanhos de entrada igualmente espaçados no intervalo [10, 10.000].
         Utiliza o valor de k para determinar o espaçamento entre os tamanhos.

- m: Número de pares de vetores gerados para cada tamanho de entrada. Este valor é o mesmo
     para todos os tamanhos e é escolhido aleatoriamente no intervalo [10, 20].
'''

times_naive = []
times_karatsuba = []

for idx, n in enumerate(sizes):
    print(f"Processando tamanho {n} ({idx + 1}/{len(sizes)})")

    # M pares de vetores de entrada aleatórios de tamanho n
    inputs = [
        ([random.randint(-2 * n, 2 * n) for _ in range(n)], [random.randint(-2 * n, 2 * n) for _ in range(n)])
        for _ in range(m)
    ]

    start_time = time.time()
    for vec1, vec2 in inputs:
        naive_multiplication(vec1, vec2)
    times_naive.append((time.time() - start_time) / m)
    
    start_time = time.time()
    for vec1, vec2 in inputs:
        karatsuba(vec1, vec2)
    times_karatsuba.append((time.time() - start_time) / m)

plt.figure(figsize=(12, 8), dpi=120)
plt.plot(sizes, times_naive, label="Multiplicação Ingênua", marker="o", linestyle="--", color="blue", linewidth=1.5)
plt.plot(sizes, times_karatsuba, label="Multiplicação de Karatsuba", marker="s", linestyle="-", color="green", linewidth=1.5)

plt.title("Comparação de Algoritmos de Multiplicação", fontsize=16, fontweight="bold")
plt.xlabel("Tamanho da Entrada (n)", fontsize=14)
plt.ylabel("Tempo de Execução (segundos)", fontsize=14)
plt.legend(fontsize=12, loc="upper left")
plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

plt.savefig("comparacao_algoritmos.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8), dpi=120)
ax.set_xlim(10, 10000)
ax.set_ylim(0, max(max(times_naive), max(times_karatsuba)) * 1.1)
ax.set_title("Evolução dos Tempos de Execução", fontsize=16, fontweight="bold")
ax.set_xlabel("Tamanho da Entrada (n)", fontsize=14)
ax.set_ylabel("Tempo de Execução (segundos)", fontsize=14)
line_naive, = ax.plot([], [], label="Multiplicação Ingênua", color="blue", marker="o", linestyle="--")
line_karatsuba, = ax.plot([], [], label="Multiplicação de Karatsuba", color="green", marker="s", linestyle="-")
ax.legend(fontsize=12, loc="upper left")
ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

def update(frame):
    '''
    Atualiza os dados para cada quadro da animação, mostrando a evolução
    dos tempos de execução conforme os tamanhos das entradas aumentam.

    Parâmetros:
        frame (int): Índice do quadro atual na animação.

    Retorno:
        line_naive, line_karatsuba: Atualizações das linhas de tempos.
    '''
    line_naive.set_data(sizes[:frame], times_naive[:frame])
    line_karatsuba.set_data(sizes[:frame], times_karatsuba[:frame])
    return line_naive, line_karatsuba

ani = FuncAnimation(fig, update, frames=len(sizes), interval=50, blit=True)
ani.save("evolucao_tempos.gif", writer="imagemagick", fps=20)
plt.show()