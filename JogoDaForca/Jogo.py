from random import choice
from time import sleep
import pygame

# Musica de fundo
pygame.init()
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.load('HoliznaCC0 - Adventure Begins Loop.mp3')
pygame.mixer.music.play(-1)
# Funcoes
lista_palavras = ['boi', 'chita', 'lesma', 'cachorro', 'baleia', 'cabra', 'gato', 'sardinha', 'pato', 'coruja']
palavra_sorteada = choice(lista_palavras)
chances = 10
tentativas = 0
letras_escohidas = []
estado_atual = ['_'] * len(palavra_sorteada)

print('-' * 30)
print('\033[7;1;40m|Jogo Da Forca |'.center(30), end='')
print('\033[m')
sleep(0.5)
print('-' * 30)
print(f'''O TEMA É ANIMAIS
Voce tem {chances} chances, Boa Sorte!!!''')
print('-' * 30)

print(f'A palavra escolhida tem {len(palavra_sorteada)} Letras.')
print(estado_atual)
# Jogo
while tentativas < chances and ''.join(estado_atual) != palavra_sorteada:

    usuario_letra = input('Adivinhe uma letra: ').lower().strip()
    # Verificar condicoes
    while True:
        if usuario_letra.isnumeric() or usuario_letra == '':
            print('\033[1;31mDigite somete letras!!\033[m\n')
            usuario_letra = input('Adivinhe uma letra: ')

        elif len(usuario_letra) > 1:
            print('\033[1;31mDigite somente uma letra de cada vez\033[m\n')
            usuario_letra = input('Adivinhe uma letra: ')
        else:
            break
    # Verificar Letra e comprar
    while usuario_letra in letras_escohidas:
        print('\033[1;33mVoce já tentou essa letra\033[m')
        usuario_letra = input('Adivinhe uma letra: ')

    letras_escohidas.append(usuario_letra)

    if usuario_letra in palavra_sorteada:
        print('\033[1;32mVOCE ACRTOU A LETRA!!\033[m')
        for i in range(len(palavra_sorteada)):
            if usuario_letra == palavra_sorteada[i]:
                estado_atual[i] = usuario_letra
    else:
        print('\033[1;31mVOCE ERROU A LETRA!!\033[m')
        tentativas += 1

    print(f'\nVoce ainda tem {chances - tentativas} chances.')
    print(f'{estado_atual}\n')
    print(f'letras já tentadas:', end=' ')

    for letra in letras_escohidas:
        print(letra, end=',')
    print()
if ''.join(estado_atual) == palavra_sorteada:
    print('\033[1;32mVOCE GANHOU !! PARABENS\033[m')
elif chances == tentativas:
    print('Voce perdeu!!'.upper())
    print(f'a palvra era: {palavra_sorteada}')
