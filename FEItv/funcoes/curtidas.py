import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def curtir_video(usuario):
    id_video = input("Digite o ID do vídeo: ")

    with open(os.path.join(BASE_DIR, "curtidas.txt"), "r") as arquivo:
        curtidas = arquivo.readlines()

    nova_curtida = f"{usuario};{id_video}\n"

    if nova_curtida in curtidas:
        curtidas.remove(nova_curtida)

        with open("curtidas.txt", "w") as arquivo:
            arquivo.writelines(curtidas)

        print("Curtida removida.")

    else:
        with open("curtidas.txt", "a") as arquivo:
            arquivo.write(nova_curtida)

        print("Vídeo curtido!")