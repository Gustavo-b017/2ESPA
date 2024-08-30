#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Importação de módulos necessários
import sys  # Módulo para manipulação de argumentos e funções do sistema
import random  # Módulo para geração de números aleatórios
import typing  # Módulo para suporte a tipos de dados avançados

# Função para ordenar uma lista usando o algoritmo Selection Sort
def selection_sort(vetor: list[any]) -> None:
    """
    Implementação do algoritmo Selection Sort.
    
    Parâmetros
    ----------
    vetor: uma lista de elementos de tipo qualquer.
    
    Retorno
    -------
    None
    """
    # Percorre cada elemento do vetor
    for i, _ in enumerate(vetor):
        indice_min = i  # Assume que o menor elemento é o atual

        # Encontra o menor elemento no restante do vetor
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[indice_min]:
                indice_min = j  # Atualiza o índice do menor elemento

        # Troca o menor elemento encontrado com o elemento atual
        vetor[i], vetor[indice_min] = vetor[indice_min], vetor[i]

# Função para ordenar uma lista usando o algoritmo Insertion Sort
def insertion_sort(vetor: list[any]) -> None:
    """
    Implementação do algoritmo Insertion Sort.

    Parâmetros
    ----------
    vetor: uma lista de elementos de tipo qualquer.
    
    Retorno
    -------
    None
    """
    # Percorre cada elemento do vetor a partir do segundo
    for i in range(1, len(vetor)):
        chave = vetor[i]  # Elemento a ser inserido na posição correta
        j = i - 1  # Índice do elemento anterior

        # Move os elementos maiores que a chave para a direita
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1

        # Insere a chave na posição correta
        vetor[j + 1] = chave

# Função para ordenar uma lista usando o algoritmo Bubble Sort
def bubble_sort(vetor: list[any]) -> None:
    """
    Implementação do algoritmo Bubble Sort.

    Parâmetros
    ----------
    vetor: uma lista de elementos de tipo qualquer.
    
    Retorno
    -------
    None
    """
    tamanho = len(vetor)  # Tamanho do vetor
    i = 0  # Índice inicial
    troca = True  # Flag para verificar se houve troca

    # Continua enquanto houver trocas e não chegar ao final do vetor
    while i < tamanho - 1 and troca:
        troca = False  # Reseta a flag de troca

        # Percorre o vetor até o penúltimo elemento não ordenado
        for j in range(tamanho - i - 1):
            if vetor[j] > vetor[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                troca = True  # Marca que houve troca

        i += 1  # Incrementa o índice

# Função para combinar dois subvetores em um vetor ordenado
def combina(vetor: list[any], esquerda: int, meio: int, direita: int) -> None:
    """
    Faz a combinação de dois subvetores de uma chamada recursiva do
    merge sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    meio:     índice que marca o meio de um subvetor.
    direita:  índice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """
    n1 = meio - esquerda + 1  # Tamanho do subvetor esquerdo
    n2 = direita - meio  # Tamanho do subvetor direito

    # Cria subvetores temporários
    subvetor_e = [vetor[esquerda + i] for i in range(n1)]
    subvetor_d = [vetor[meio + 1 + j] for j in range(n2)]
    i = j = 0  # Índices iniciais dos subvetores
    k = esquerda  # Índice inicial do vetor combinado

    # Combina os subvetores em ordem crescente
    while i < n1 and j < n2:
        if subvetor_e[i] <= subvetor_d[j]:
            vetor[k] = subvetor_e[i]
            i += 1
        else:
            vetor[k] = subvetor_d[j]
            j += 1
        k += 1

    # Copia os elementos restantes do subvetor esquerdo, se houver
    while i < n1:
        vetor[k] = subvetor_e[i]
        i += 1
        k += 1

    # Copia os elementos restantes do subvetor direito, se houver
    while j < n2:
        vetor[k] = subvetor_d[j]
        j += 1
        k += 1

# Função para ordenar uma lista usando o algoritmo Merge Sort
def merge_sort(vetor: list[any], esquerda: int, direita: int) -> None:
    """
    Implementação do algoritmo Merge Sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  índice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """
    if esquerda < direita:
        meio = esquerda + (direita - esquerda) // 2  # Calcula o meio do vetor
        merge_sort(vetor, esquerda, meio)  # Ordena a primeira metade
        merge_sort(vetor, meio + 1, direita)  # Ordena a segunda metade
        combina(vetor, esquerda, meio, direita)  # Combina as duas metades

# Função para particionar um vetor para o algoritmo Quick Sort
def particiona(vetor: list[any], esquerda: int, direita: int) -> int:
    """
    Implementação do algoritmo particiona

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  índice que marca o fim de um subvetor.
    
    Retorno
    -------
    int
        índice de onde está o elemento pivot
    """
    pivot = vetor[direita]  # Escolhe o último elemento como pivot
    i = esquerda - 1  # Índice do menor elemento

    # Percorre o vetor e rearranja os elementos em relação ao pivot
    for j in range(esquerda, direita):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]  # Troca os elementos

    vetor[i + 1], vetor[direita] = vetor[direita], vetor[i + 1]  # Coloca o pivot na posição correta

    return i + 1  # Retorna o índice do pivot

# Função para ordenar uma lista usando o algoritmo Quick Sort
def quick_sort(vetor: list[any], esquerda: int, direita: int) -> None:
    """
    Implementação do algoritmo Quick Sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  índice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """
    if esquerda < direita:
        pivot = particiona(vetor, esquerda, direita)  # Particiona o vetor
        quick_sort(vetor, esquerda, pivot - 1)  # Ordena a primeira metade
        quick_sort(vetor, pivot + 1, direita)  # Ordena a segunda metade

# Função para verificar se um vetor está ordenado
def verifica_vetor_ordenado(vetor: list[any]) -> bool:
    """
    Verifica se um vetor está ordenado

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    
    Retorno
    -------
    bool
        Retorna True se o vetor está ordenado, caso contrário, retorna
        False
    """
    # Percorre o vetor e verifica se cada elemento está em ordem
    for i in range(1, len(vetor)):
        if vetor[i - 1] > vetor[i]:
            return False  # Retorna False se encontrar um elemento fora de ordem

    return True  # Retorna True se todos os elementos estiverem em ordem

# Bloco principal para testar as funções de ordenação
if __name__ == "__main__":
    random.seed(42)  # Define a semente para geração de números aleatórios

    if len(sys.argv) > 1:
        n = int(sys.argv[1])  # Obtém o tamanho do vetor a partir dos argumentos da linha de comando
    else:
        n = 100  # Define o tamanho padrão do vetor como 100

    V = [random.randint(1, n) for _ in range(n)]  # Gera um vetor de tamanho n com números aleatórios
    merge_sort(V, 0, len(V) - 1)  # Ordena o vetor usando Merge Sort
    assert verifica_vetor_ordenado(V)  # Verifica se o vetor está ordenado
    print(V)  # Imprime o vetor ordenado