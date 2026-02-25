import webbrowser

playlist = []
def linha():
    print("==============================================")

def nova_musica():
    artista = str(input("Qual o artista ou banda que fez a música? "))
    nome_musica = str(input("Qual o nome da música? "))
    ano_lancamento = int(input("Qual o ano de lançamento da música? "))
    plataforma = str(input("Qual a plataforma de streaming da música? "))
    url = input("Insira o link da música: ")
    
    musicas = {
        'artista' : artista,
        'nome_musica' : nome_musica,
        'ano_lancamento' : ano_lancamento,
        'plataforma' : plataforma,
        'URL' : url
    }
    playlist.append(musicas)

def tocar_playlist():
    if not playlist:
        print("Nenhuma música na playlist!")
        return False
    
    print("Verifique a playlist para conferir o indice da música!")
    indice = int(input("Qual o índice da música: ")) 
    webbrowser.open(playlist[indice - 1]['URL'])
    
def ver_playlist():
    if not playlist:
        print("Nenhuma música na playlist!")
        return False
        
    for i in range(len(playlist)):  
        print(f"Indice {i+1}")
        print(f"Artista: {playlist[i]['artista']}")
        print(f"Nome da música: {playlist[i]['nome_musica']}")
        print(f"Ano de Lançamento: {playlist[i]['ano_lancamento']}")
        print(f"Plataforma: {playlist[i]['plataforma']}")
        print(f"URL: {playlist[i]['URL']}")
        print("\n")
    return True

def remover_musica():
    print()
    if not playlist:
        print("Não há música na playlist!")
        return
    
    ver_playlist()
    try:
        indice = int(input("Digite o indice da música que deseja remover: "))
        
        if indice > 0:
            playlist.pop(indice - 1) #arrumar isto, já que o o indice é mostrado a partir de um, mas não coincide com a posicao na lista, que no caso é 0
            print(f"Música {indice} removida!")
        else:
            print("Número inválido!")
            
    except ValueError:
        print("Erro: Insira um valor válido!")
    
def avaliacao(a): 
    a = int(input("Avalie a playlist de 1 a 5: "))
    match a:
        case 1:
            print(("⭐"))
            print("Vamos melhorar na próxima! 😓")
        case 2:
            print("⭐⭐")
            print("Estamos aprimorando para mehlor experiência! 😉")
        case 3:
            print("⭐⭐⭐")
            print("Agradecemos pela avaliação positiva! 😁")
        case 4:
            print("⭐⭐⭐⭐")
            print("Batemos na trave, mas agradecemos a avaliação positiva! 😉👌")
        case 5: 
            print("⭐⭐⭐⭐⭐")
            print("Pelo visto a experiência foi ótima, esperamos lhe ver novamente! 🥰")

while True:
    linha()
    print("\t\t  Playlist")
    linha()
    print("1 - Adicionar músicas para a playlist")
    print("2 - Tocar playlist")
    print("3 - Ver playlist")
    print("4 - Remover uma música da playlist")
    print("5 - Avaliar a playlist")
    print("6 - Sair")
    linha()
    play = int(input("Selecione uma opção: "))
    linha()
    match play:
        case 1: 
            nova_musica()
        case 2:
            tocar_playlist()
        case 3: 
            ver_playlist()
        case 4:
            remover_musica()
        case 5: 
            avaliacao(0)
        case 6:
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")