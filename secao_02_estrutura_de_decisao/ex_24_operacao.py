"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


from msvcrt import open_osfhandle


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    operadores = {'+': operador.add, '-': operador.sub, '*': operador.mlt, '/': operador.div}
    operacao_funcao = operadores[operacao]
    resultado = operacao_funcao(n_1, n_2)

    resultado_str = str(resultado)
    resultado_tipo = 'inteiro'
    if '.' in resultado_str:
        parte_decimal = int(resultado_str.split('.')[-1])
    if int(parte_decimal) != 0:
        resultado_tipo = 'decimal'
        sinal = 'neutro'
    if resultado > 0:
        sinal = 'positivo'
    elif resultado < 0:
        sinal = 'negativo'
        print(f'Resultado: {resultado:.2f}')
    if resultado_tipo == 'decimal':
        print(f'Número é {sinal} e decimal.')
    else:
        paridade = 'par' if resultado % 2==0 else 'impar'
        print(f'Número é {paridade}, {sinal} e inteiro.')