"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
<<<<<<< HEAD
    import math

    area_a_ser_pintada = int(input('Digite a área, em metros quadrados a ser pintada:'))
    area_com_folga = area_a_ser_pintada * 1.1
    litros_a_serem_usados = math.ceil(area_com_folga / 6)
    numero_de_latas = math.ceil(litros_a_serem_usados / 18)
    valor_com_apenas_latas = numero_de_latas * 80
    litros_restantes_com_latas = float(numero_de_latas * 18) - litros_a_serem_usados
    print (f'Você deve comprar {litros_a_serem_usados} litros de tinta.')
    print(f'Você pode comprar {numero_de_latas} lata(s) de 18 litros a um custo de R$ {valor_com_apenas_latas}. Vão sobrar {litros_restantes_com_latas} litro(s) de tinta.')
    

    numero_de_galoes = math.ceil(litros_a_serem_usados / 3.6)
    valor_com_apenas_galoes = numero_de_galoes * 25
    litros_restantes_com_galoes = float(numero_de_galoes * 3.6) - litros_a_serem_usados
    print(f'Você pode comprar {numero_de_galoes} lata(s) de 3.6 litros a um custo de R$ {valor_com_apenas_galoes}. Vão sobrar {litros_restantes_com_galoes:.1f} litro(s) de tinta.')

    numero_de_latas = math.floor(litros_a_serem_usados / 18)
    valor_de_latas = numero_de_latas * 80
    litros_faltantes = litros_a_serem_usados % 18
    numero_de_galoes = math.ceil(litros_faltantes/ 3.6)
    valor_com_galoes = numero_de_galoes * 25

    valor_total = valor_de_latas + valor_com_galoes
    litros_restantes_total = float(numero_de_galoes * 3.6) + (numero_de_latas * 18) - litros_a_serem_usados
    print(f'Para menor custo, você pode comprar {numero_de_latas} lata(s) de 18 litros e {numero_de_galoes} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar {litros_restantes_total:.1f} litro(s) de tinta.')
=======
    area_a_ser_pintada = float(input('Qual a área, em metros quadrados, que você quer pintar? '))
    area_a_ser_pintada_com_folga = area_a_ser_pintada * 1.1
    quantidade_de_tinta_em_litros = math.ceil(area_a_ser_pintada_com_folga / 6)
    (desperdicio_apenas_com_latas_de_18_litros, quantidade_apenas_latas_de_tinta_18_litros,valor_apenas_com_latas_de_18_litro) = calcular_recipientes_custo_e_desperdicio (quantidade_de_tinta_em_litros,
        18,
        80
    )
    (
        desperdicio_apenas_com_latas_de_3_6_litros,
        quantidade_apenas_latas_de_tinta_3_6_litros,
        valor_apenas_com_latas_de_3_6_litros
    ) = calcular_recipientes_custo_e_desperdicio(
        quantidade_de_tinta_em_litros,
        3.6,
        25
    )

    # Tirar uma lata de 18 litros
    (
        desperdicio_otimo_com_latas_de_18_litros,
        quantidade_otima_latas_de_tinta_18_litros,
        valor_otimo_com_latas_de_18_litros
    ) = calcular_recipientes_custo_e_desperdicio(
        quantidade_de_tinta_em_litros - 18,
        18,
        80
    )

    # Calcular galoes de 3.6 para a sobra
    (
        desperdicio_otimo_com_latas_de_3_6_litros,
        quantidade_otima_latas_de_tinta_3_6_litros,
        valor_otimo_com_latas_de_3_6_litros
    ) = calcular_recipientes_custo_e_desperdicio(
        18 - desperdicio_otimo_com_latas_de_18_litros,
        3.6,
        25
    )

    valor_otimo = valor_otimo_com_latas_de_3_6_litros + valor_otimo_com_latas_de_18_litros

    print(f'Você deve comprar {quantidade_de_tinta_em_litros:.0f} litros de tinta.')
    print(
        f'Você pode comprar {quantidade_apenas_latas_de_tinta_18_litros} lata(s) de 18 litros a um custo de'
        f' R$ {valor_apenas_com_latas_de_18_litros}. '
        f'Vão sobrar {desperdicio_apenas_com_latas_de_18_litros:.1f} litro(s) de tinta.'
    )
    print(
        f'Você pode comprar {quantidade_apenas_latas_de_tinta_3_6_litros} lata(s) de 3.6 litros a um custo de'
        f' R$ {valor_apenas_com_latas_de_3_6_litros}. '
        f'Vão sobrar {desperdicio_apenas_com_latas_de_3_6_litros:.1f} litro(s) de tinta.'
    )
    print(f'Para menor custo, você pode comprar {quantidade_otima_latas_de_tinta_18_litros} lata(s) de 18 litros e' f' {quantidade_otima_latas_de_tinta_3_6_litros} galão(ões) de 3.6 litros a um custo de R$ {valor_otimo}. ' f'Vão sobrar {desperdicio_otimo_com_latas_de_3_6_litros:.1f} litro(s) de tinta.'
    )


def calcular_recipientes_custo_e_desperdicio(quantidade_de_tinta_em_litros, litros_por_recipiente,
        preco_por_recipiente):
    quantidade_de_recipientes, resto_de_tinta_em_litros = divmod(
        quantidade_de_tinta_em_litros, litros_por_recipiente
    )
    if resto_de_tinta_em_litros == 0:
        quantidade_de_final_de_recipientes = int(quantidade_de_recipientes)
        desperdicio = 0
    else:
        quantidade_de_final_de_recipientes = int(quantidade_de_recipientes + 1)
        desperdicio = litros_por_recipiente - resto_de_tinta_em_litros
    valor = preco_por_recipiente * quantidade_de_final_de_recipientes
    return desperdicio, quantidade_de_final_de_recipientes, valor
>>>>>>> bd06c11b34b3bf1ccd6a6019ce540edf10aeaec2

