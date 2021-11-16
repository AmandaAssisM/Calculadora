import calculator

while True:
    number_1, number_2 = calculator.pegar_entrada_usuario()
    opcao = calculator.pegar_opcao_menu()
    calculator.verificar_opcao(opcao, number_1, number_2)
    

    continuar = ' '
    while continuar not in 'YN':
        continuar = input('Do you want to calculate again? Please type Y for YES or N for NO. ').strip().upper()[0]

    if continuar == 'N':
        break
