import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def listar_videos():
    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    print("=== VÍDEOS ===")

    for video in videos:
        dados = video.strip().split(";")

        print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def buscar_video():
    print("=== BUSCAR VÍDEO ===")
    print("1 - Buscar por nome")
    print("2 - Buscar por ID")
    print("3 - Buscar por tipo")
    print("4 - Buscar por gênero")

    opcao = input("Escolha: ")

    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    encontrado = False

    if opcao == "1":
        busca = input("Digite o nome do vídeo: ").lower()

        for video in videos:
            dados = video.strip().split(";")

            if busca in dados[1].lower():
                encontrado = True

                print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

    elif opcao == "2":
        busca = input("Digite o ID do vídeo: ")

        for video in videos:
            dados = video.strip().split(";")

            if busca == dados[0]:
                encontrado = True

                print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

    elif opcao == "3":
        busca = input("Digite o tipo do vídeo: ").lower()

        for video in videos:
            dados = video.strip().split(";")

            if busca == dados[2].lower():
                encontrado = True

                print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

    elif opcao == "4":
        busca = input("Digite o gênero do vídeo: ").lower()

        for video in videos:
            dados = video.strip().split(";")

            if busca == dados[3].lower():
                encontrado = True

                print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

    else:
        print("Opção inválida.")
        return

    if not encontrado:
        print("Vídeo não encontrado.")