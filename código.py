#importar bibliotecas que vão ser utilizadas
#os = limpar o terminal e random para tema/palavra aleatória
import os
import random
from unidecode import unidecode # Importa a função unidecode da biblioteca unidecode
import pygame

#fazer uma variavel imagem!
#imagem =  : caminho da imagem

#Apresentação e escolha
print('Olha! Bem-vindo ao jogo da forca!')

#opções
def exibir_menu():
    print("1. Palavra aleatória")
    print("2. Seu amigo escolhe o tema e a palavra")

exibir_menu()
mododejogar = input('Qual modo quer jogar? ')

#dicionario de palavras, para gerar a aleatoriedade
temas = {
    'animal': ['vaca', 'peixe', 'pássaro', 'ovelha', 'cachorros', 'gato', 'leão', 'hipopotamo'],
    'fruta' : ['banana', 'maçã', 'laranja', 'abacaxi', 'milho', 'morango', 'pera'],
    'legume' : ['alface', 'cenoura', 'abóbora', 'brócolis', 'ervilha', 'batata'],
    'objeto': ['celular', 'caneta', 'copo', 'linha', 'cama', 'quadro', 'lâmpada'],
    'paises' : ['alemanha', 'brasil', 'frança', 'estados unidos', 'china', 'japão', 'canadá'],
    'cores' : ['amarelo', 'cinza', 'branco', 'vermelho', 'azul', 'verde', 'roxo'],
}

while True:
    exibir_menu()
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
        continue

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
    #definir armazenamento das tentativas
    tentativa = input('Digite uma letra: ').lower() #lower(): deixar as letras minúsculas

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
    
        #verificar se o número de tentativas erradas foi atingidas
        if tentativas_erradas == max_letrasincorrect:
            print('Infelizmente, acabou suas tentativas')
            print('A palavra era', palavra)
            break

    historico_letras.append(unidecode(tentativa))

    #palavra descoberta, quando for descoberta
    palavra_descoberta = ''.join(l if unidecode(l) in letracorrect else "_" for l in palavra)
    print("Palavra:", palavra_descoberta)

    # Verifica se todas as letras foram adivinhadas
    if all(unidecode(letra) in letracorrect for letra in palavra):
        print("Parabéns! Você adivinhou as letras da palavra corretamente:", palavra)
        break

#Aperfeiçoamento: Colocar a letra mesmo com acento: concluido
#Aperfeiçoamento: quando a pessoa digitar a mesma letra, falar "já foi essa letra, tente novamente": concluido
