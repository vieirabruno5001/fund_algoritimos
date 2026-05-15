import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def listar_videos():
    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    print("\n=== VÍDEOS ===")

    for video in videos:
        dados = video.strip().split(";")

        print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

def buscar_video():
    nome = input("Digite o nome do vídeo: ").lower()

    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    encontrado = False

    for video in videos:
        dados = video.strip().split(";")

        if nome in dados[1].lower():
            encontrado = True

            print(f"""
ID: {dados[0]}
Nome: {dados[1]}
Tipo: {dados[2]}
Gênero: {dados[3]}
""")

    if not encontrado:
        print("Vídeo não encontrado.")