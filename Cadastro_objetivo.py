import os

cadastro_individual = []

os.system('cls')
print('Planeje como alcançar o seu sonho')
print
plano = input('Qual o seu sonho em uma palavra: ')
custo = input('Qual o custo para realizar o seu sonho? ')

while True:
    while True:
        os.system('cls')
        opcao = input('Escolha uma opção: (i)Inserir  (r)Retirar  (l)Listar  (f)Finalizar: ')

        if opcao == 'i':
            os.system('cls')
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            renda = float(input('Renda mensal: '))
            gasto = float(input('Gasto mensal: '))
            cadastro_individual.append([
                nome, 
                idade, 
                renda,
                gasto
            ])
        
        elif opcao == 'r':
            indice_str = int(input('Escolha o indice que será retirada: '))
            try:
                indice = int(indice_str)
                del cadastro_individual[indice]
            except ValueError:
                print('Por favor digite um número inteiro')
            except IndexError:
                print('Índice não existe na lista')

        elif opcao == 'l':
            os.system('cls')
            numeracao = 0
            if len(cadastro_individual) == 0:
                print('Nada para listar')
            for i in cadastro_individual:
                numeracao += 1
                print(numeracao, end=' - ')
                for detalhe in i:
                    print(detalhe , end='  ') # arrumar uma forma de printar todas as informações em uma linha
                print('')

        elif opcao == 'f':
            os.system('cls')
            numeracao = 0
            if len(cadastro_individual) == 0:
                print('Nada para listar')
            for i in cadastro_individual:
                numeracao += 1
                print(numeracao, end=' - ')
                for detalhe in i:
                    print(detalhe , end='  ')
                print('')
            break
        
        else:
            print('Por favor, escolha i, a ou l ou f para finalizar')

        print()

        renda_total = 0
        for i in cadastro_individual:
            if len(i) > 2:
                renda_total += float(i[2])
        print('A renda total do grupo é: ', renda_total)

        gasto_total = 0
        for i in cadastro_individual:
            if len(i) > 3:
                gasto_total += float(i[3])
        print('O gasto total do grupo é: ',renda_total)

    if len(cadastro_individual) == 0:
        break   
    else:
        resultado = renda_total - gasto_total

    if resultado <= 0:
        print('Reajuste os gastos mensais ou aumente a renda mensal do grupo para alcançar o objetivo estabelecido!')
    else:
        tempo = int(custo) // resultado
        tempo2 = tempo // 12
        print('De acordo com as rendas e gastos mensais atuais, o ojbetivo será alcançada em aproximadamente', int(tempo2), 'anos!')

    print()

    repetir = input('Deseja fazer um novo planejamento? (s)Sim  (n)Não: ')
    if repetir == 's':
        for _ in range(len(cadastro_individual)):
            cadastro_individual.clear()
        continue
    else:
        break
