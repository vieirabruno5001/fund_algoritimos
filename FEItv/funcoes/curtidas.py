import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def curtir_video(usuario):
    id_video = input("Digite o ID do vídeo: ")

    with open(os.path.join(BASE_DIR, "videos.txt"), "r") as arquivo:
        videos = arquivo.readlines()

    video_encontrado = False

    for video in videos:
        dados = video.strip().split(";")

        if dados[0] == id_video:
            video_encontrado = True
            break

    if not video_encontrado:
        print("Vídeo não encontrado.")
        return

    with open(os.path.join(BASE_DIR, "curtidas.txt"), "r") as arquivo:
        curtidas = arquivo.readlines()

    nova_curtida = f"{usuario};{id_video}\n"

    if nova_curtida in curtidas:
        curtidas.remove(nova_curtida)

        with open(os.path.join(BASE_DIR, "curtidas.txt"), "w") as arquivo:
            arquivo.writelines(curtidas)

        print("Curtida removida.")

    else:
        with open(os.path.join(BASE_DIR, "curtidas.txt"), "a") as arquivo:
            arquivo.write(nova_curtida)

        print("Vídeo curtido!")