from funcoes import *
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

print(frota)  
