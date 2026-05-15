import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from funcoes.usuarios import cadastrar_usuario, login
from funcoes.videos import buscar_video, listar_videos
from funcoes.curtidas import curtir_video
from funcoes.favoritos import menu_favoritos

usuario_logado = None

while True:
    print("\n===== FEItv =====")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Listar vídeos")
    print("4 - Buscar vídeo")
    print("5 - Curtir vídeo")
    print("6 - Favoritos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        usuario_logado = login()

    elif opcao == "3":
        listar_videos()

    elif opcao == "4":
        buscar_video()

    elif opcao == "5":
        if usuario_logado:
            curtir_video(usuario_logado)
        else:
            print("Faça login primeiro.")

    elif opcao == "6":
        if usuario_logado:
            menu_favoritos(usuario_logado)
        else:
            print("Faça login primeiro.")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")