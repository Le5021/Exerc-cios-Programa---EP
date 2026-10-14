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

def define_posicoes (linha, coluna, orientacao, tamanho): #define_posicoes(0, 1, "vertical", 3)
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
define_posicoes(0, 1, "vertical", 3) 