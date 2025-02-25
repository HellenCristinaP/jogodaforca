#importar bibliotecas que vão ser utilizadas
#os = limpar o terminal e random para tema/palavra aleatória
import os
import random
from unidecode import unidecode # Importa a função unidecode da biblioteca unidecode

#fazer uma variavel imagem!
#imagem =  : caminho da imagem

#Apresentação e escolha
print('Olha! Bem-vindo ao jogo da forca!')

#opções
def exibir_menu():
    print("1. Palavra aleatória")
    print("2. Seu amigo escolhe o tema e a palavra")

#dicionario de palavras, para gerar a aleatoriedade
temas = {
    'animal': ['vaca', 'peixe', 'pássaro', 'ovelha', 'cachorros', 'gato', 'leão', 'hipopotamo'],
    'fruta' : ['banana', 'maçã', 'laranja', 'abacaxi', 'milho', 'morango', 'pera'],
    'legume' : ['alface', 'cenoura', 'abóbora', 'brócolis', 'ervilha', 'batata'],
    'objeto': ['celular', 'caneta', 'copo', 'linha', 'cama', 'quadro', 'lâmpada'],
    'paises' : ['alemanha', 'brasil', 'frança', 'estados unidos', 'china', 'japão', 'canadá'],
    'cores' : ['amarelo', 'cinza', 'branco', 'vermelho', 'azul', 'verde', 'roxo'],
}

exibir_menu()

tentativasdomodo = 0

while True:
    mododejogar = input('Qual modo quer jogar? ')
    
    if mododejogar == "1":
        #Quero que pegue uma categoria e palavra aleatoria
        tema = random.choice(list(temas.keys()))
        palavra = random.choice(temas[tema])
        break
    elif mododejogar == "2":
        #definir tema e palavra
        tema = input("Qual o tema? ")
        palavra = input("Qual a palavra? ")
        break
    else:
        #voltar, virando uma repetição
        print("Escolha não identificada")
        tentativasdomodo += 1

    if tentativasdomodo == 3:
        print('')
        print("Digite ou 1 ou 2! POR FAVOR!")
        print('')
    elif tentativasdomodo == 4:
        print('')
        print("Está de brincadeira com a minha cara?!")
        print('')
    elif tentativasdomodo == 5:
        print('')
        print("Pode ficar assim o quanto quiser, não falo mais nada")
        print('')    
    elif tentativasdomodo >= 6:
        print("Infelizmente, acabou o jogo")
        break

#armazenar a palavra e as letras
letra = list(unidecode(palavra)) #remove os acentos
historico_letras = []
letracorrect = []

#maximo de tentativas
max_letrasincorrect = (7)

#contador de tentativas erradas
tentativas_erradas = (0)

os.system("cls")

#falar o tema e as tentativas
print('o tema é', tema if mododejogar == '2' else tema)
print('Você tem 7 tentativas')

#repetição:
while True:
    
    palavra_descoberta = ''.join(l if unidecode(l) in letracorrect else "_ " for l in palavra)
    print('Palavra: ', palavra_descoberta)
    print(" ")

    #definir armazenamento das tentativas
    tentativa = input('Digite uma letra: ').lower() #lower(): deixar as letras minúsculas

    if tentativa == palavra:
        print('Parabéns! Você adivinhou a palavra corretamente:', palavra)
        #quebrar o loop sem sair do programa, mas voltar ao início
        break


    #verificar se é letra única
    #significado de isalpha():verificar se tem string=! ou len():verificar o números de elementos enviados=1
    if not tentativa.isalpha() or len(tentativa) !=1:
        print('Por favor, insira somente uma letra!')
        continue

    if unidecode(tentativa) in historico_letras:
        print('Você já tentou essa letra antes!')
        continue

    #Se a tentativar for coerrente, letra correta, se não, letra incorreta
    if tentativa in letra:
        letracorrect.append(unidecode(tentativa))
        print('Letra correta!')
    else:
        print('Letra incorreta, tente novamente')
        tentativas_erradas += 1
        print('Tentativas erradas: ', tentativas_erradas)
    
        #verificar se o número de tentativas erradas foi atingidas
        if tentativas_erradas == max_letrasincorrect:
            print('Infelizmente, acabou suas tentativas')
            print('A palavra era', palavra)

    historico_letras.append(unidecode(tentativa))

    # Verifica se todas as letras foram adivinhadas
    if all(unidecode(letra) in letracorrect for letra in palavra):
        print("Parabéns! Você adivinhou a palavra corretamente:", palavra)
    historico_letras.append(unidecode(tentativa))

    # Verifica se todas as letras foram adivinhadas
    if all(unidecode(letra) in letracorrect for letra in palavra):
        print("Parabéns! Você adivinhou a palavra corretamente:", palavra)
