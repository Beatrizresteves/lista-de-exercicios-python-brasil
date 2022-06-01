"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    if letra == 'a':
        return 'vogal'
    if letra == 'e':
        return 'vogal'
    if letra == 'i':
        return 'vogal'
    if letra == 'o':
        return 'vogal'
    if letra == 'u':
        return 'vogal'
    if letra == 'A':
        return 'vogal'
    if letra == 'E':
        return 'vogal'
    if letra == 'I':
        return 'vogal'
    if letra == 'O':
        return 'vogal'
    if letra == 'U':
        return 'vogal'
    else:
        return 'consoante'