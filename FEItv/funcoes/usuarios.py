import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    with open(os.path.join(BASE_DIR, "usuarios.txt"), "a") as arquivo:
        arquivo.write(f"{nome};{email};{senha}\n")

    print("Usuário cadastrado com sucesso!")


def login():
    email = input("Email: ")
    senha = input("Senha: ")

    with open(os.path.join(BASE_DIR, "usuarios.txt"), "r") as arquivo:
        usuarios = arquivo.readlines()

    for usuario in usuarios:
        dados = usuario.strip().split(";")

        if dados[1] == email and dados[2] == senha:
            print("Login realizado!")
            return email

    print("Email ou senha incorretos.")
    return None