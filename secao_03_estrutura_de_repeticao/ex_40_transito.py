"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    import math
    maior_indice = 0
    codigo_maior_indice = 0
    menor_indice = 100_000_000_000
    codigo_menor_indice = 0
    total_de_veiculos = 0
    cidades_mais_de_150_mil = 0
    acidentes_cidades_mais_de_150_mil = 0

    for codigo, veiculos, acidentes in cidades:
        indice_acidentes = (acidentes * 1000) / veiculos
        if indice_acidentes > maior_indice:
            maior_indice = indice_acidentes
            codigo_maior_indice = codigo
        if indice_acidentes < menor_indice:
            menor_indice = round(indice_acidentes, 1)
            codigo_menor_indice = codigo

        total_de_veiculos += veiculos

        if veiculos <= 150_000:
            cidades_mais_de_150_mil += 1
            acidentes_cidades_mais_de_150_mil += acidentes
            media_acidentes = acidentes_cidades_mais_de_150_mil/cidades_mais_de_150_mil

    print(f'O maior índice de acidentes é de {codigo_maior_indice}, com {maior_indice} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {codigo_menor_indice}, com {menor_indice} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {total_de_veiculos/5:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acidentes:.1f} acidentes.')


