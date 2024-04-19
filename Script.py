import csv


def adicionar_cliente(nome, email, telefone):
    with open('clientes.csv', mode='a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([nome, email, telefone])
    print("Cliente adicionado com sucesso!")


def visualizar_clientes():
    with open('clientes.csv', mode='r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for cliente in leitor_csv:
            print("Nome:", cliente[0])
            print("Email:", cliente[1])
            print("Telefone:", cliente[2])
            print("----------------------")


def buscar_cliente(nome):
    with open('clientes.csv', mode='r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        encontrado = False
        for cliente in leitor_csv:
            if cliente[0] == nome:
                print("Cliente encontrado:")
                print("Nome:", cliente[0])
                print("Email:", cliente[1])
                print("Telefone:", cliente[2])
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")


def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar cliente")
        print("2. Visualizar clientes")
        print("3. Buscar cliente")
        print("4. Encerrar programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_cliente(nome, email, telefone)
        elif escolha == '2':
            visualizar_clientes()
        elif escolha == '3':
            nome = input("Digite o nome do cliente a ser buscado: ")
            buscar_cliente(nome)
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
