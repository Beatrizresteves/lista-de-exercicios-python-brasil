"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia 5 números e informe o maior número.

    >>> calcular_maior_numero(1, 2, 3, 4, 5)
    5
    >>> calcular_maior_numero(-1, -30, -20, -15, -2)
    -1
"""


def calcular_maior_numero(n1: int, n2: int, n3: int, n4: int, n5: int, ) -> int:
    """Escreva aqui em baixo a sua solução"""
    if n1 > n2:
        print(n1)
    elif n2 > n3:
        print(n2)
    elif n3 > n4:
        print(n3)
    elif n4 > n5:
        print(n4)
    elif n5 > n1:
        print(n5)