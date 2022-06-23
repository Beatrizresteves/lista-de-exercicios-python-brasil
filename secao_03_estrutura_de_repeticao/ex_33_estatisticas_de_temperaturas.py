"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""
    maior_temperatura = 'não existe'
    menor_temperatura = 'não existe'
    soma = 0
    media = 0
    if len(temperaturas) == 0:
        maior_temperatura = menor_temperatura = media = 'não existe'
    else:
        for i in temperaturas:
            if maior_temperatura == 'não existe':
                maior_temperatura = menor_temperatura = i 
            if maior_temperatura < i:
                maior_temperatura = i
            if menor_temperatura > i:
                menor_temperatura = i
            soma += i
            divisor = len(temperaturas)
            media = (soma / divisor)
            media = f'{media:.1f}'
    return f'Maior temperatura: {maior_temperatura}. Menor temperatura: {menor_temperatura}. Média: {media}'