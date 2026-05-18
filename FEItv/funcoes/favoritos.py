import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def menu_favoritos(usuario):
    while True:
        print("=== FAVORITOS ===")
        print("1 - Adicionar vídeo")
        print("2 - Ver favoritos")
        print("3 - Remover vídeo")
        print("0 - Voltar")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_favorito(usuario)

        elif opcao == "2":
            ver_favoritos(usuario)

        elif opcao == "3":
            remover_favorito(usuario)

        elif opcao == "0":
            break


def adicionar_favorito(usuario):
    nome_video = input("Nome do vídeo: ")

    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    video_encontrado = False

    for video in videos:
        dados = video.strip().split(";")

        if dados[1] == nome_video:
            video_encontrado = True
            break

    if not video_encontrado:
        print("Vídeo não encontrado.")
        return

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "a") as arquivo:
        arquivo.write(f"{usuario};{nome_video}\n")

    print("Vídeo adicionado aos favoritos.")

def ver_favoritos(usuario):
    with open(os.path.join(BASE_DIR, "favoritos.txt"), "r") as arquivo:
        favoritos = arquivo.readlines()

    encontrou = False

    print("=== SEUS FAVORITOS ===")

    for favorito in favoritos:
        dados = favorito.strip().split(";")

        if dados[0] == usuario:
            encontrou = True
            print(f"Nome: {dados[1]}")

    if not encontrou:
        print("Você não adicionou nenhum vídeo aos favoritos.")


def remover_favorito(usuario):
    nome_video = input("Nome do vídeo para remover: ")

    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    video_encontrado = False

    for video in videos:
        dados = video.strip().split(";")

        if dados[1] == nome_video:
            video_encontrado = True
            break

    if not video_encontrado:
        print("Vídeo não encontrado.")
        return

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "r") as arquivo:
        favoritos = arquivo.readlines()

    removido = False

    with open(os.path.join(BASE_DIR, "favoritos.txt"), "w") as arquivo:
        for favorito in favoritos:
            dados = favorito.strip().split(";")

            if dados[0] == usuario and dados[1] == nome_video:
                removido = True
                continue

            arquivo.write(favorito)

    if removido:
        print("Vídeo removido dos favoritos.")
    else:
        print("Esse vídeo não está nos favoritos.")