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

linha = 1
coluna = 1
orientacao = "vertical"
tamanho = 2

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

def preenche_frota (dicionario_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)
    if nome_navio in dicionario_frota:
        dicionario_frota[nome_navio].append(posicoes)
    else:
        dicionario_frota[nome_navio] = [posicoes]

    return dicionario_frota

tabuleiro = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

linha = 1
coluna = 1
resultado = faz_jogada(tabuleiro, linha, coluna)
print(resultado)