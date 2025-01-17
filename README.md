# PROJETO 1: Algoritmo de Karatsuba vs. Multiplicação Ingênua

Este repositório contém a implementação, análise e documentação comparativa entre o **algoritmo de multiplicação ingênua** e o **algoritmo de Karatsuba**. O objetivo é explorar as diferenças em termos de complexidade computacional.

---

## 📋 Descrição

A multiplicação de inteiros grandes é uma operação fundamental em diversas áreas da ciência da computação. Neste projeto, comparamos duas abordagens principais:

1. **Multiplicação Ingênua**: Abordagem direta com complexidade temporal de $O(n^2)$.
2. **Algoritmo de Karatsuba**: Método baseado em divisão e conquista, reduzindo a complexidade para $O(n^{\log_2 3})$.

As implementações foram realizadas em Python, com suporte a números de precisão arbitrária, e avaliadas quanto ao desempenho para diferentes tamanhos de entrada.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**: Linguagem de programação utilizada para implementar os algoritmos.
- **Matplotlib**: Biblioteca usada para gerar os gráficos comparativos.
- **LaTeX**: Ferramenta utilizada para a elaboração do relatório técnico.

---

## 📁 Funcionalidades

- **Cálculo de Tempos de Execução**: O código executa ambos os algoritmos em diferentes tamanhos de entrada, gerando tempos de execução para cada um.
- **Gráficos Comparativos**: Geração de gráficos que comparam o tempo de execução dos dois algoritmos com base no tamanho da entrada.
- **Animação da Evolução dos Tempos**: Um GIF é gerado para mostrar a evolução dos tempos de execução ao longo do aumento do tamanho das entradas.


---

## 📊 Resultados

Os gráficos a seguir ilustram os principais resultados:

### Crescimento Assintótico

![Gráfico Comparativo](report/comparacao_algoritmos.png)

### Visualização Interativa

![Evolução dos Tempos](report/evolucao_tempos.gif)

O GIF demonstra a evolução dos tempos de execução à medida que o tamanho da entrada aumenta.
