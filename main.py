# Exercicio 1
print('EX1')
nomes = []

def menu1():
    print("Escolha uma opção:")
    print('(1) Cadastrar um amigo (no final da lista)')
    print('(2) Mostrar os nomes de todos os amigos')
    print('(9) Sair do programa')

    n = int(input("Opção selecionada: "))

    while n != 1 and n != 2 and n != 9:
        print("Essa opção é inválida!")
        n = int(input("Digite a opção selecionada: "))

    if n == 1:
        nomeadd = str(input("Nome do amigo a ser cadastrado: "))
        nomes.append(nomeadd)
        menu1()
    if n == 2:
        print(nomes)
        menu1()
    if n == 9:
        print("Saindo do programa!")

menu1()

# Exercicio 2
print('EX2')

nomes = []

def menu2():
    print("Escolha uma opção:")
    print('(1) Cadastrar um amigo (no final da lista)')
    print('(2) Mostrar os nomes de todos os amigos')
    print('(3) Cadastrar um amigo (no inicio da lista)')
    print('(4) Remover um nome')
    print('(5) Substituir um nome')
    print('(6) Mostrar o número total de amigos cadastrados')
    print('(7) Colocar os nomes dos amigos em ordem alfabética')
    print('(9) Sair do programa')

    n = int(input("Opção selecionada: "))

    while n < 1 or n > 9 or n == 8:
        print("Essa opção é inválida!")
        n = int(input("Digite a opção selecionada: "))

    if n == 1:
        nomeadd = str(input("Nome do amigo a ser cadastrado: "))
        nomes.append(nomeadd)
        menu2()

    if n == 2:
        if len(nomes) < 1:
            print('A lista está vazia!')
            menu2()
        print(nomes)
        menu2()

    if n == 3:
        nomeadd = str(input("Nome do amigo a ser cadastrado: "))
        nomes.insert(0, nomeadd)
        menu2()

    if n == 4:
        if len(nomes) < 1:
            print('A lista está vazia!')
            menu2()
        print(nomes)
        try:
            numerodel = int(input('Digite o número da posição que você deseja apagar (lembrando que 0 é o primeiro): '))
        except ValueError:
            print('Valor inválido, por favor use um número. Voltando ao menu.')
            menu2()

        print(f"O nome {nomes[numerodel]} foi removido. Gostaria de ver a lista (1) ou voltar diretamente ao menu (9)?")
        del nomes[numerodel]
        resp = int(input("Digite sua opção: "))
        while resp != 1 and resp != 9:
            print("Essa opção é inválida!")
            resp = int(input("Digite a opção selecionada: "))
        if resp == 1:
            print(nomes)
            menu2()
        if resp == 9:
            menu2()
    if n == 5:
        if len(nomes) < 1:
            print('A lista está vazia!')
            menu2()
        print(nomes)
        try:
            numerosubs = int(input('Digite o número da posição que você deseja substituir (lembrando que 0 é o primeiro): '))
        except ValueError:
            print('Valor inválido, por favor use um número. Voltando ao menu.')
            menu2()
        subs = str(input(f"Você selecionou a opção: {nomes[numerosubs]}. Pelo o que você substituir? "))
        print(f'O nome {nomes[numerosubs]} foi substituido com sucesso para: {subs}. Gostaria de ver a lista (1) ou voltar diretamente ao menu (9)?')
        nomes[numerosubs] = subs
        while resp != 1 and resp != 9:
            print("Essa opção é inválida!")
            resp = int(input("Digite a opção selecionada: "))
        if resp == 1:
            print(nomes)
            menu2()
        if resp == 9:
            menu2()
    if n == 6:
        if len(nomes) < 1:
            print('A lista está vazia!')
            menu2()
        print(f'Número total de amigos cadastrados: {len(nomes)}')
        menu2()
    if n == 7:
        if len(nomes) < 1:
            print('A lista está vazia!')
            menu2()
        print('A lista foi organizada com sucesso!')
        nomes.sort()
    if n == 9:
        print("Saindo do programa!")

menu2()