import time
import random


def linha():
    print('-' * 13)


def mostrar_jogo_da_velha():
    for i in campo:
        print(i)


def marcar_posicao(posicao, simbolo):
    count1 = 0
    for lista in campo:
        count2 = 0
        for i in lista:
            if i == posicao:
                campo[count1][count2] = simbolo
                numeros_jogados.append(posicao)
                break
            count2 += 1
        count1 += 1


def pc_joga(pc_simbolo):
    posicao = random.randint(1, 9)
    while posicao in numeros_jogados:
        posicao = random.randint(1, 9)
        if len(numeros_jogados) == 9:
            break
    marcar_posicao(posicao, pc_simbolo)


def verificar_ganho_horizontal(simbolo):
    for lista in campo:
        repitidos = 0
        for i in lista:
            if i != simbolo:
                break
            repitidos += 1
        if repitidos == 3:
            mostrar_jogo_da_velha()
            print('jogador {} ganhou'.format(simbolo))
            exit()


def verificar_ganho_diagonal(simbolo):
    repitidos = 0
    if campo[0][0] == simbolo:
        repitidos += 1
    if campo[1][1] == simbolo:
        repitidos += 1
    if campo[2][2] == simbolo:
        repitidos += 1
    if repitidos == 3:
        mostrar_jogo_da_velha()
        print('Jogador {} ganhou'.format(simbolo))
        exit()
    else:
        repitidos = 0
        if campo[0][2] == simbolo:
            repitidos += 1
        if campo[1][1] == simbolo:
            repitidos += 1
        if campo[2][0] == simbolo:
            repitidos += 1
        if repitidos == 3:
            mostrar_jogo_da_velha()
            print('Jogador {} ganhou'.format(simbolo))
            exit()


def verificar_ganho_vertical(simbolo, coluna=0):
    repitidos = 0
    count = 0
    for linha in campo:
        if linha[coluna] == simbolo:
            repitidos += 1
        else:
            if coluna < 2:
                coluna += 1
                verificar_ganho_vertical(simbolo, coluna)
    if repitidos == 3:
        mostrar_jogo_da_velha()
        print('Jogador {} ganhou'.format(simbolo))
        exit()




linha()
print('Jogo da velha')
linha()
campo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numeros_jogados = list()
posicao = 0
linha()
mostrar_jogo_da_velha()
linha()

start = str(input('Deseja começar? (s/n)')).lower()
if start == 's':
    print('primeira rodada')
    print('Começando o jogo...')
    time.sleep(0)
    simbolo = str(input('Voce deseja ser X ou o O?')).upper()
    if simbolo == 'X':
        pc_simbolo = 'O'
    else:
        pc_simbolo = 'X'
elif start == 'n':
    print('Até a proxima!')
    exit()
else:
    print('Eu nao te entendo')
while start == 's':
    mostrar_jogo_da_velha()
    posicao = int(input('onde você deseja jogar?'))
    while posicao in numeros_jogados:
        posicao = int(input('onde você deseja jogar?'))
    marcar_posicao(posicao, simbolo)
    verificar_ganho_horizontal(simbolo)
    verificar_ganho_diagonal(simbolo)
    verificar_ganho_vertical(simbolo)
    pc_joga(pc_simbolo)
    verificar_ganho_horizontal(pc_simbolo)
    verificar_ganho_diagonal(pc_simbolo)
    verificar_ganho_vertical(pc_simbolo)


