def pegar_entrada_usuario():
    while True:
        try:
            number_1 = float(input('Enter your first number: '))
            number_2 = float(input('Enter your second number: '))
            
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número válido.')
            continue

        return number_1, number_2


def pegar_opcao_menu():
    menu()
    opcao = input('Digite sua opção: ')
    return opcao


def menu():
    print('''
    [+] for addition
    [-] for subtraction
    [*] for multiplication
    [/] for division''')


def verificar_opcao(opcao, number_1, number_2):
    opções_validas = ['+', '-', '*', '/']

    while  opcao not in opções_validas:
        print('Insira uma opção válida.')
        opcao = input('Digite sua opção: ')

    if opcao == '+':
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
                
    elif opcao == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    elif opcao == '*':
        print(f'{number_1} x {number_2} = {number_1 * number_2}')

    elif opcao == '/':
        print(f'{number_1} / {number_2} = {number_1 / number_2}')
