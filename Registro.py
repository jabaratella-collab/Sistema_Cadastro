import re
import json
import os

ARQUIVO_DADOS = "banco_dados.json"
usuarios = []


def carregar_dados():
    global usuarios
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            try:
                usuarios = json.load(arquivo)
                print(f"Dados carregados: {len(usuarios)} usuários.")
            except json.JSONDecodeError:
                usuarios = []
                print("Arquivo de dados vazio ou corrompido.")
    else:
        usuarios = []


def salvar_dados():
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def cadastrar():
    print("\n===== Novo Cadastro =====")

    nome = input("Digite seu nome: ")
    while len(nome.strip().split()) < 2:
        print("Nome inválido! Digite nome e sobrenome.")
        nome = input("Digite seu nome: ")

    cpf = input("Digite seu cpf (xxx.xxx.xxx-xx): ")

    while not re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
        print("CPF inválido! Use o formato xxx.xxx.xxx-xx.")
        cpf = input("Digite seu cpf: ")

    while any(u["cpf"] == cpf for u in usuarios):
        print("CPF já cadastrado!")
        cpf = input("Digite outro cpf: ")
        while not re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
            print("CPF inválido! Use o formato xxx.xxx.xxx-xx.")
            cpf = input("Digite seu cpf: ")

    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    while not re.fullmatch(r"\d{2}/\d{2}/\d{4}", data_nascimento):
        print("Data inválida! Formato correto: dd/mm/aaaa.")
        data_nascimento = input("Digite sua data de nascimento: ")

    email = input("Digite seu email: ")

    telefone = input("Digite seu telefone (9 números): ")
    while not (telefone.isdigit() and len(telefone) == 9):
        print("Telefone inválido! Deve ter 9 números.")
        telefone = input("Digite seu telefone: ")

    naturalidade = input("Digite sua naturalidade: ")
    endereco = input("Digite seu endereço: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu estado: ")

    novo_usuario = {
        'nome': nome,
        'cpf': cpf,
        'data de nascimento': data_nascimento,
        'email': email,
        'telefone': telefone,
        'naturalidade': naturalidade,
        'endereco': endereco,
        'bairro': bairro,
        'cidade': cidade,
        'estado': estado
    }

    usuarios.append(novo_usuario)
    salvar_dados()
    print("\nUsuário cadastrado com sucesso!")


def pesquisar():
    print("\n====== Pesquisar ======")
    cpf = input("Digite o CPF do usuário que deseja encontrar: ")

    for pessoa in usuarios:
        if pessoa['cpf'] == cpf:
            print("\nUsuário encontrado:")

            for chave, valor in pessoa.items():
                print(f"{chave.capitalize()}: {valor}")
            return pessoa

    print("\nUsuário não encontrado.")

    return None


def atualizar():
    print("\n====== Atualizar Usuário ======")
    cpf = input("Digite o CPF do usuário que deseja atualizar: ")

    for pessoa in usuarios:
        if pessoa["cpf"] == cpf:
            print("\nDeixe em branco para manter o valor atual.\n")

            for chave in pessoa:

                if chave == 'cpf':
                    continue

                novo = input(f"{chave} ({pessoa[chave]}): ")
                if novo != "":
                    pessoa[chave] = novo

            salvar_dados()
            print("\nUsuário atualizado!")
            return

    print("\n Usuário não encontrado.")


def excluir():
    print("\n====== Excluir Usuário ======")
    cpf = input("Digite o CPF do usuário que deseja excluir: ")

    for pessoa in usuarios:
        if pessoa["cpf"] == cpf:
            usuarios.remove(pessoa)
            salvar_dados()
            print("\nUsuário excluído!")
            return

    print("\nUsuário não encontrado.")


carregar_dados()

while True:
    print("\n===== Menu Principal =====")
    print("1. Cadastrar")
    print("2. Pesquisar")
    print("3. Excluir")
    print("4. Atualizar")
    print("5. Sair do Programa")
    print("")

    x = input("Escolha uma opção: ")

    match x:
        case '1':
            cadastrar()
        case '2':
            pesquisar()
        case '3':
            excluir()
        case '4':
            atualizar()
        case '5':
            print("Programa encerrado. Dados salvos.")
            break
        case _:
            print("Opção inválida! Tente outra vez.")