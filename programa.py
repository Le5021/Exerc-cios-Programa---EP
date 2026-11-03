from funcoes import *
from random import randint 

#Questão 7: 

navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
} 

frota = {}   

for NOME, TAMANHO in navios.items(): 
    tamanho_navio = TAMANHO[0]
    quantidade_navio = TAMANHO[1] 
    
    contagem_navios_validos = 0 

    while contagem_navios_validos < quantidade_navio: 
        
        print(f"Insira as informações referentes ao navio {NOME} que possui tamanho {tamanho_navio}")    

        linha = int(input("Linha: "))
        while linha < 0 or linha > 9: 
            print("Esta posição não está válida!")
            linha = int(input("Linha: ")) 

        coluna = int(input("Coluna: "))
        while coluna < 0 or coluna > 9:
                print("Esta posição não está válida!")
                coluna = int(input("Coluna: ")) 

        if NOME != "submarino": 
            orientacao = input("[1] Vertical [2] Horizontal > ")

            while orientacao != "1" and orientacao != "2":
                print("Esta posição não está válida!")
                orientacao = input("[1] Vertical [2] Horizontal > ") 
            
            if orientacao == "1": 
                    orientacao = "vertical"
            elif orientacao == "2":
                    orientacao = "horizontal"
        else: 
            orientacao = "vertical" 

        posicoes_validas =  posicao_valida(frota, linha, coluna, orientacao, tamanho_navio)

        if posicoes_validas:
            frota = preenche_frota (frota, NOME, linha, coluna, orientacao, tamanho_navio) 
            contagem_navios_validos += 1 
        else: 
             print("Esta posição não está válida!")  


#Questão 8:

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota (frota_oponente)
tabuleiro_jogador = posiciona_frota (frota)

posicoes_usadas_jogador = []

# Adição para a Questão 9:
posicoes_usadas_oponente = [] 

while True:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto 

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:

        ataque_linha = int(input('Jogador, qual linha deseja atacar? '))

        while ataque_linha < 0 or ataque_linha > 9:
            print('Linha inválida!')
            ataque_linha = int(input('Jogador, qual linha deseja atacar? '))

        ataque_coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while ataque_coluna < 0 or ataque_coluna > 9:
            print('Coluna inválida!')
            ataque_coluna = int(input('Jogador, qual coluna deseja atacar? '))


        posicao_informada = [ataque_linha, ataque_coluna]

        for posicoes in posicoes_usadas_jogador:
            if posicoes[0] == ataque_linha and posicoes[1] == ataque_coluna:
                print('A posição linha', ataque_linha,'e coluna', ataque_coluna,'já foi informada anteriormente!')
                  
        else:
            posicoes_usadas_jogador.append(posicao_informada)
            break

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, ataque_linha, ataque_coluna)

    frota_quantidade = 0
    for valor in frota_oponente.values():
        for lista in valor:
            frota_quantidade += 1

    if afundados(frota_oponente, tabuleiro_oponente) == frota_quantidade:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break

# Questão 9: 
    else:
        ataque_linha_op = randint(0, 9)
        ataque_coluna_op = randint(0, 9) 

        posicao_informada_op = [ataque_linha_op, ataque_coluna_op]
        
        for posicoes in posicoes_usadas_oponente: 
            if posicoes[0] == ataque_linha_op and posicoes[1] == ataque_coluna_op:
                ataque_linha_op = randint(0, 9)
                ataque_coluna_op = randint(0, 9) 

            else: 
                posicoes_usadas_oponente.append(posicao_informada_op) 
                print(f'Seu oponente está atacando na linha {ataque_linha_op} e coluna {ataque_coluna_op}') 
                break 


        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, ataque_linha_op, ataque_coluna_op) 

        frota_jogador = 0 
        for valor in frota.values():
            for lista in valor: 
                frota_jogador += 1 

        if afundados(frota, tabuleiro_jogador) == frota_jogador: 
            print('Xi! O oponente derrubou toda a sua frota =(') 
            break 