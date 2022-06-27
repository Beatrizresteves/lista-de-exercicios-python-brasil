"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    cliente_mais_gordo = 0
    cliente_mais_magro = 0
    cliente_mais_alto = 0
    cliente_mais_baixo = 0
    peso_mais_gordo = 0
    peso_mais_magro = 1000
    altura_mais_alto = 0
    altura_mais_baixo = 500
    soma_dos_pesos = 0
    soma_das_alturas = 0
    quantidade_de_clientes = 0

    while True:
        cliente = input('Digite o nome do cliente:')
        if cliente == "0":
            break
        quantidade_de_clientes += 1
        altura = int(input('Digite a altura do cliente (em centímetros): '))
        peso = float(input('Digite o peso do cliente (em kg): '))

        soma_dos_pesos += peso
        soma_das_alturas += altura

        if altura > altura_mais_alto:
            altura_mais_alto = altura
            cliente_mais_alto = cliente

        if altura < altura_mais_baixo:
            altura_mais_baixo = altura
            cliente_mais_baixo = cliente

        if peso > peso_mais_gordo:
            peso_mais_gordo = peso
            cliente_mais_gordo = cliente

        if peso < peso_mais_magro:
            peso_mais_magro = peso
            cliente_mais_magro = cliente

    media_das_alturas = soma_das_alturas / quantidade_de_clientes
    media_dos_pesos = soma_dos_pesos / quantidade_de_clientes

    print(f'Cliente mais alto: {cliente_mais_alto}, com {altura_mais_alto} centímetros')
    print(f'Cliente mais baixo: {cliente_mais_baixo}, com {altura_mais_baixo} centímetros')
    print(f'Cliente mais magro: {cliente_mais_magro}, com {peso_mais_magro:.0f} kilos')
    print(f'Cliente mais gordo: {cliente_mais_gordo}, com {peso_mais_gordo:.0f} kilos')
    print(f'--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_das_alturas:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_dos_pesos:.1f} kilos')