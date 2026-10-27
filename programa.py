grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

#Questão 1: 

def define_posicoes (linha, coluna, orientacao, tamanho): 
    posicao_final = []

    if orientacao == "vertical":
        coluna_final = coluna 
        linha_final = linha
        i = 0
        while i < tamanho:
            linha_final = linha + i 
            posicao_final.append([linha_final, coluna_final]) 
            i += 1 

    elif orientacao == "horizontal":
        linha_final = linha
        coluna_final = coluna 
        j = 0 
        while j < tamanho:
            coluna_final = coluna + j 
            posicao_final.append([linha_final, coluna_final]) 
            j += 1 

    return posicao_final


# Questão 2: 

def preenche_frota (dicionario_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)
    if nome_navio in dicionario_frota:
        dicionario_frota[nome_navio].append(posicoes)
    else:
        dicionario_frota[nome_navio] = [posicoes]

    return dicionario_frota

# Questão 3: 

# tabuleiro = [
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
#   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#   [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# ]

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

# linha = 1
# coluna = 1
# resultado = faz_jogada(tabuleiro, linha, coluna)
# print(resultado)


# Questão 4:
 
def posiciona_frota (dicionario_posicoes):
    tabuleiro_final = [[0] * 10 for _ in range(10)] #criando o tabuleiro
    for chaves, valor in dicionario_posicoes.items(): #lista 1 do valor
        for posicoes in valor: #lista 2 do valor
            for coordenadas in posicoes: #lista 3 do valor
                tabuleiro_final[coordenadas[0]][coordenadas[1]] = 1 #linha + coluna = 1

    return tabuleiro_final


#Questão 5:
 
#tabuleiro = [
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
#   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#   [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# ]
# resultado = afundados(frota, tabuleiro)
# print(resultado)

def afundados(frota, tabuleiro): 
    contagem_navios_afundados = 0  

    for chaves, valor in frota.items(): 
        for posicoes in valor: 
            posicao_atingida = 0  
            for coordenadas in posicoes: 
                if tabuleiro[coordenadas[0]][coordenadas[1]] == 'X': 
                    posicao_atingida += 1 
                
            if posicao_atingida == len(posicoes):
                contagem_navios_afundados += 1 

    return contagem_navios_afundados 


#Questão 6: 

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes =  define_posicoes (linha, coluna, orientacao, tamanho)
    tabuleiro = posiciona_frota(frota) 
    contagem_validos = 0 

    for coordenadas in posicoes: 
        if 0 <= coordenadas[0] and coordenadas[0] < 10 and 0 <= coordenadas[1] and coordenadas[1] < 10 and tabuleiro[coordenadas[0]][coordenadas[1]] == 0:
                contagem_validos += 1 

        if contagem_validos == len(posicoes):
            return True
        
    return False 

#Questão 7: 

navios = {
    "porta-avioes": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
} 

frota = {}   

for NOME, TAMANHO in navios.items(): 
    tamanho_navio = TAMANHO[0]
    quantidade_navio = TAMANHO[1] 

    mensagem_principal = print(f"Insira as informações referentes ao navio {NOME} que possui tamanho {tamanho_navio}")   
    contagem_navios_validos = 0 

    while contagem_navios_validos < quantidade_navio:  

        linha = int(input("Linha: "))
        while linha < 0 or linha > 9: #Não colocar para verificar na função "Posições válidas", senão ele só retorna True ou False
            print("Esta posição não está válida!")
            linha = int(input("Linha: ")) 

        coluna = int(input("Coluna: "))
        while coluna < 0 or coluna > 9:
                print("Esta posição não está válida!")
                coluna = int(input("Coluna: ")) 

        if NOME != "submarino": 
            orientacao = input("[1] Vertical [2] Horizontal > ")

            if orientacao != 1 and orientacao != 2:
                print("Esta posição não está válida!")
                orientacao = input("[1] Vertical [2] Horizontal > ") 
            else: 
                if orientacao == 1: 
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
        else: 
            orientacao = "vertical" 

        posicoes_validas =  define_posicoes (linha, coluna, orientacao, tamanho_navio)

        if posicoes_validas == True: 
            frota = preenche_frota (frota, NOME, linha, coluna, orientacao, tamanho_navio) 
            contagem_navios_validos += 1 
        else: 
            print("Esta posição não está válida!") 

        print(frota) 
