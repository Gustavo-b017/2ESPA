#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
import sys
import random
import typing


## Implementação de Funções - - - - - - - - - - - - - - - - - - - - - #
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

    for i,_ in enumerate(vetor):
        indice_min = i

        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[indice_min]:
                indice_min = j

        vetor[i], vetor[indice_min] = vetor[indice_min], vetor[i]


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

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i -1

        while j >=0 and vetor[j] > chave:
            vetor[j +1] = vetor[j]
            j -= 1

        vetor[j +1] = chave


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

    tamanho = len(vetor)
    i = 0
    troca = True

    while i < tamanho -1 and troca != False:
        troca = False

        for j in range(tamanho -i -1):
            if vetor[j] > vetor[j +1]:
                vetor[j], vetor[j +1] = vetor[j +1], vetor[j]
                troca = True

        i += 1


def combina(vetor: list[any],
            esquerda: int,
            meio: int,
            direita: int) -> None:
    """
    Faz a combinação de dois subvetores de uma chamada recursiva do
    merge sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    meio:     índice que marca o meio de um subvetor.
    direita:  ídnice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """

    n1 = meio - esquerda +1
    n2 = direita - meio

    subvetor_e = [vetor[esquerda +i] for i in range(n1)]
    subvetor_d = [vetor[meio +1 +j]  for j in range(n2)]
    i = j = 0
    k = esquerda

    while i < n1 and  j < n2:
        if subvetor_e[i] <= subvetor_d[j]:
            vetor[k] = subvetor_e[i]
            i += 1

        else:
            vetor[k] = subvetor_d[j]
            j += 1

        k += 1

    while i < n1:
        vetor[k] = subvetor_e[i]
        i += 1
        k += 1

    while j < n2:
        vetor[k] = subvetor_d[j]
        j += 1
        k += 1

def merge_sort(vetor: list[any], esquerda: int, direita: int) -> None:
    """
    Implementação do algoritmo Merge Sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  ídnice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """

    if esquerda < direita:
        meio = esquerda + (direita - esquerda) // 2
        merge_sort(vetor, esquerda, meio)
        merge_sort(vetor, meio +1, direita)
        combina(vetor, esquerda, meio, direita)


def particiona(vetor: list[any],
               esquerda: int,
               direita: int) -> int :
    """
    Implementação do algoritmo particiona

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  ídnice que marca o fim de um subvetor.
    
    Retorno
    -------
    int
        índice de onde está o elemento pivot
    """
    pivot = vetor[direita]
    i = esquerda -1

    for j in range(esquerda, direita):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i +1], vetor[direita] = vetor[direita], vetor[i +1]

    return i +1


def quick_sort(vetor: list[any],
               esquerda: int,
               direita: int) -> None:
    """
    Implementação do algoritmo Qucik Sort.

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    esquerda: índice que marca o início de um subvetor.
    direita:  ídnice que marca o fim de um subvetor.
    
    Retorno
    -------
    None
    """

    if esquerda < direita:
        pivot = particiona(vetor, esquerda, direita)
        quick_sort(vetor, esquerda, pivot -1)
        quick_sort(vetor, pivot +1, direita)


def verifica_vetor_ordenado(vetor: list[any]) -> bool:
    """
    Verifica se um vetor está ordenado

    Parâmetros
    ----------
    vetor:    uma lista de elementos de tipo qualquer.
    
    Retorno
    -------
    bool
        Retorna True se o vetor está ordenado, caso contrário, retona
        False
    """

    for i in range(1, len(vetor)):
        if vetor[i -1] > vetor[i]:
            return False

    return True


## verifica se a implementação de um algoritmo está correta - - - - - #
if __name__ == "__main__":
    random.seed(42)

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 100

    V = [random.randint(1, n) for _ in range(n)]
    merge_sort(V, 0, len(V) -1)
    assert verifica_vetor_ordenado(V)
    print(V)
