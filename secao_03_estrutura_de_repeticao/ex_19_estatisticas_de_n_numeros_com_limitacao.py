"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""

    for i in numeros:
        if not (0 <= i <= 1000):
            return 'Somente números de 0 a 1000 são permitidos'
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