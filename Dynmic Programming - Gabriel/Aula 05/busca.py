#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
import sys
import typing
import random


## Implementação de funções - - - - - - - - - - - - - - - - - - - - - #
def busca_sequencial(vetor: list[any], x: any) -> int:
    """
    Implementação do algoritmo de busca sequencial.

    Parâmetro(s)
    -----------
    vetor: uma lista de elementos de qualquer tipo.
    x:     um elemento a ser procurado na lista vetor (assume-se que
           seja do mesmo tipo dos elementos do vetor)

    Retorno
    -------
    int
        Se o elemento x foi encontrado na vetor, então retorna o índice
        i tal que x == vetor[i]. Caso contrário, x não foi encontrado
        em vetor, retona -1
    """
    for i, elemento in enumerate(vetor):
        if elemento == x:
            return i

    return -1


def busca_binaria_iterativa(vetor: list[any],
                            esquerdo: int,
                            direito: int,
                            x: int) -> int:
    """
    Implementação recursiva do algoritmo de busca binária.

    Parâmetro(s)
    -----------
    vetor: uma lista de elementos de qualquer tipo.
    x:     um elemento a ser procurado na lista vetor (assume-se que
           seja do mesmo tipo dos elementos do vetor)

    Retorno
    -------
    int
        Se o elemento x foi encontrado na vetor, então retorna o índice
        i tal que x == vetor[i]. Caso contrário, x não foi encontrado
        em vetor, retona -1
    """

    while esquerdo <= direito:
        meio = esquerdo + (direito - esquerdo) // 2

        if vetor[meio] == x:
            return meio

        elif vetor[meio] < x:
            esquerdo = meio +1

        else:
            direito = meio -1

    return -1


def busca_binaria_recursiva(vetor: list[any],
                            esquerdo: int,
                            direito: int,
                            x: int) -> int:
    """
    Implementação recursiva do algoritmo de busca binária.

    Parâmetro(s)
    -----------
    vetor: uma lista de elementos de qualquer tipo.
    x:     um elemento a ser procurado na lista vetor (assume-se que
           seja do mesmo tipo dos elementos do vetor)

    Retorno
    -------
    int
        Se o elemento x foi encontrado na vetor, então retorna o índice
        i tal que x == vetor[i]. Caso contrário, x não foi encontrado
        em vetor, retona -1
    """

    if esquerdo > direito:
        return -1

    else:
        meio = (esquerdo + direito) // 2
        if vetor[meio] == x:
            return meio

        elif x > vetor[meio]:
            return busca_binaria_recursiva(vetor, meio +1, direito, x)
        else:
            return busca_binaria_recursiva(vetor, esquerdo, meio -1, x)


## Código para testar a implementação - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    if len(sys.argv) > 1:
        tamanho = int(sys.argv)
    else:
        tamanho = 100

    random.seed(42)
    vetor = [random.randint(0, tamanho) for _ in range(tamanho)]
    vetor.sort()
    x = vetor[-1]
    # busca um elemento que pertence ao vetor
    assert busca_binaria_iterativa(vetor, 0, len(vetor) -1, x) != -1
    x = tamanho +1
    # busca um elemento que não pertence ao vetor
    assert busca_binaria_iterativa(vetor, 0, len(vetor) -1, x) == -1
