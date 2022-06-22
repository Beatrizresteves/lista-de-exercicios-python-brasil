"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior valor: 2. Menor valor: -1. Soma: 2'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    soma = 0
    maior_numero = 'não existe'
    menor_numero = 'não existe'
    for i in numeros:
        if maior_numero == 'não existe':
            menor_numero = maior_numero = i 
        if maior_numero < i:
            maior_numero = i
        if menor_numero > i:
            menor_numero = i
        soma += i
    return f'Maior valor: {maior_numero}. Menor valor: {menor_numero}. Soma: {soma}'