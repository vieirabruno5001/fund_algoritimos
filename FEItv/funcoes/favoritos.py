import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def menu_favoritos(usuario):
    while True:
        print("\n=== FAVORITOS ===")
        print("1 - Adicionar vídeo")
        print("2 - Ver favoritos")
        print("3 - Remover vídeo")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_favorito(usuario)

        elif opcao == "2":
            ver_favoritos(usuario)

        elif opcao == "3":
            remover_favorito(usuario)

        elif opcao == "0":
            break


def adicionar_favorito(usuario):
    id_video = input("ID do vídeo: ")

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "a") as arquivo:
        arquivo.write(f"{usuario};{id_video}\n")

    print("Vídeo adicionado aos favoritos.")


def ver_favoritos(usuario):
    with open(os.path.join(BASE_DIR, "favoritos.txt"), "r") as arquivo:
        favoritos = arquivo.readlines()

    print("\n=== SEUS FAVORITOS ===")

    for favorito in favoritos:
        dados = favorito.strip().split(";")

        if dados[0] == usuario:
            print(f"Nome do vídeo: {dados[2]}")


def remover_favorito(usuario):
    id_video = input("ID do vídeo para remover: ")

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "r") as arquivo:
        favoritos = arquivo.readlines()

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "w") as arquivo:
        for favorito in favoritos:
            dados = favorito.strip().split(";")

            if not (dados[0] == usuario and dados[1] == id_video):
                arquivo.write(favorito)

    print("Vídeo removido dos favoritos.")