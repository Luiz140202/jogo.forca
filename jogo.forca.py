import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "programacao", "tendencias", "python", "codigos", "computador", "internet", "logica"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    forca = [
        '''
           +---+
               |
               |
               |
              ===''',
        '''
           +---+
           O   |
               |
               |
              ===''',
        '''
           +---+
           O   |
           |   |
               |
              ===''',
        '''
           +---+
           O   |
          /|   |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          /    |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          / \  |
              ==='''
    ]
    return forca[tentativas]

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    letras_tentadas = []
    tentativas = 0
    
    print("Seja bem-vindo ao Jogo da Forca!")
    
    while tentativas < 6:
        print("\nPalavra: " + " ".join(palavra_oculta))
        letra = input("Digite a letra escolhida: ").lower()
        
        if letra in letras_tentadas:
            print("Você já usou esta letra. Escolha outra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
            print("Letra incorreta! Você tem mais {} tentativas.".format(6 - tentativas))
        
        print(exibir_forca(tentativas))
        
        if '_' not in palavra_oculta:
            print("Parabéns! Você acertou a palavra: " + palavra)
            break
        
    if '_' in palavra_oculta:
        print("Você perdeu! A palavra certa era: " + palavra)
    
    print("Obrigado por jogar!")

jogar()
