# NOME DO CANDIDATO: Gabriel Freitas Costantin
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Estruturas e Movimento

import math


#=================================================================

# Globais importantes

bola=False 
# array de classes 
nos_atuais = []

# array de tuplas 
nos_proibidos = []
nos_perigosos = []

# Classe de nós 
class No_Atual:
    def __init__(self,x_atual,y_atual,caminho_atual,custo_acumulativo,custo_atual):
        self.x_atual = x_atual
        self.y_atual = y_atual
        self.caminho_atual = caminho_atual
        self.custo_acumulativo = custo_acumulativo
        self.custo_atual = custo_atual
        self.caminho_atual.append((x_atual,y_atual))
        
    def testar_no_atual(self):
        return(self.x_atual,self.y_atual)

    def add_no_atual(self):
        nos_atuais.append(self)

    def add_proximos_nos(self,nos_atuais,nos_proibidos,x_objetivo,y_objetivo,x_max,y_max):

        if((self.x_atual + 1, self.y_atual) not in nos_proibidos and self.x_atual + 1 < x_max and self.y_atual <= y_max ):
            x_temporario = self.x_atual + 1
            y_temporario = self.y_atual
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,1),1,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario =  custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual , self.y_atual + 1) not in nos_proibidos and self.x_atual <= x_max and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual 
            y_temporario = self.y_atual + 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,3),1,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual - 1 , self.y_atual ) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual <= y_max ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual 
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,5),1,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual  , self.y_atual - 1) not in nos_proibidos and self.x_atual <= x_max and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual 
            y_temporario = self.y_atual - 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,7),1,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual + 1, self.y_atual + 1) not in nos_proibidos and self.x_atual + 1 < x_max and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual + 1
            y_temporario = self.y_atual + 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,2),2,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual - 1 , self.y_atual + 1) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual + 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,4),2,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual - 1 , self.y_atual - 1) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual - 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,6),2,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual + 1  , self.y_atual - 1) not in nos_proibidos and self.x_atual + 1 < x_max and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual + 1
            y_temporario = self.y_atual - 1
            custo_acumulativo_temporario = self.custo_acumulativo + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,8),2,bola)
            custo_instantaneo_temporario = calcular_custo_distancia(x_temporario,y_temporario, x_objetivo, y_objetivo)
            caminho_temporario = self.caminho_atual.copy()
            custo_temporario = custo_acumulativo_temporario + custo_instantaneo_temporario
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_acumulativo_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))


                
        nos_atuais.remove(self)

# Essa função serve para calcular os pesos instantaneos 
def func_calcular_custo(x_analisado, y_analisado, x_objetivo, y_objetivo, mudanca, tipo, tem_bola):

    
    #Parametros para ajuste fino
    
    reta = 1 #nivel basico
    diagonal = 1.42 #nivel basico
    custo_proximidade_obstaculo = 0 #nivel basico

    linha_reta = 0 #nivel 1
    curva_pequena = 0.5 #nivel 1
    graus90 = 0.9 #nivel 1
    curva_antidiagonal = 1.2 #nivel 1
    graus180 = 1.7 #nivel 1
   

    peso_da_bola = 2.0 #nivel 2

    custo_proximidade_obs=2.4 #nivel 3

    #logica --------------

    if(tem_bola == False):
        peso_bola = 1
    if(tem_bola == True):
       peso_bola = peso_da_bola 


    if(tipo == 1):
        custo_tipo = reta 
    if(tipo == 2):
        custo_tipo = diagonal

    if(mudanca == 0):# linha reta
        custo_movimento = linha_reta 
    elif(mudanca == 1 or mudanca == 7):# linha diagonal proxima
        custo_movimento = curva_pequena 
    elif(mudanca == 2 or mudanca == 6):# 90 gruas
        custo_movimento = graus90 
    elif(mudanca == 3 or mudanca == 5):# anti diagonal 
        custo_movimento = curva_antidiagonal 
    elif(mudanca == 4): # 180
        custo_movimento = graus180 

    if((x_analisado, y_analisado) in nos_perigosos):
        custo_proximidade_obstaculo = custo_proximidade_obs

    custo = custo_tipo + custo_movimento * peso_bola + custo_proximidade_obstaculo * peso_bola 
    return custo


def calcular_custo_distancia(x_analisado, y_analisado, x_objetivo, y_objetivo):
    custo_distancia = math.sqrt( math.pow(x_analisado - x_objetivo,2) + math.pow(y_analisado - y_objetivo,2))
    return custo_distancia


def func_mudou_direção(caminho, direcao_antiga):

    if len(caminho)>1:

        ultimo_no = caminho[len(caminho)-1]
        penultimo_no = caminho[len(caminho)-2]


        x_u,y_u = ultimo_no
        x_pe,y_pe = penultimo_no

        direcao_atual=0

        if((x_u - x_pe) == 1 and (y_u - y_pe) == 0):
            direcao_atual=1

        elif((x_u - x_pe) == 1 and (y_u - y_pe) == 1):
            direcao_atual=2

        elif((x_u - x_pe) == 0 and (y_u - y_pe) == 1):
            direcao_atual=3

        elif((x_u - x_pe) == -1 and (y_u - y_pe) == 1):
            direcao_atual=4

        elif((x_u - x_pe) == -1 and (y_u - y_pe) == 0):
            direcao_atual=5

        elif((x_u - x_pe) == -1 and (y_u - y_pe) == -1):
            direcao_atual=6

        elif((x_u - x_pe) == 0 and (y_u - y_pe) == -1):
            direcao_atual=7

        elif((x_u - x_pe) == 1 and (y_u - y_pe) == -1):
            direcao_atual=8

        mudanca=abs(direcao_atual-direcao_antiga)

        return (mudanca)
    
    else:
        return 0




def gerar_nos_perigosos(obstaculos):
    for obs in obstaculos:
        x_temp,y_temp = obs
        nos_perigosos.append(( x_temp + 1 , y_temp))
        nos_perigosos.append(( x_temp + 1 , y_temp + 1))
        nos_perigosos.append(( x_temp, y_temp + 1 ))
        nos_perigosos.append(( x_temp - 1 , y_temp +1 ))
        nos_perigosos.append(( x_temp - 1 , y_temp ))
        nos_perigosos.append(( x_temp - 1, y_temp - 1))
        nos_perigosos.append(( x_temp , y_temp - 1 ))
        nos_perigosos.append(( x_temp + 1, y_temp - 1 ))
    return 0


# ==============================================================================================================
# Função principal
def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
 

    #setup -------------------------------------------------
    nos_atuais.clear()
    nos_proibidos.clear()
    nos_perigosos.clear()
    obs=obstaculos
    x_max = largura_grid
    y_max = altura_grid
    x_inicial, y_inicial = pos_inicial
    x_objetivo , y_objetivo = pos_objetivo
    nos_proibidos.extend(obstaculos)
    caminho_inicial = [] 
    No = No_Atual (x_inicial, y_inicial,caminho_inicial,0,0)
    No.add_no_atual()
    nos_atuais.sort(key=lambda c: c.custo_atual)
    caminho_otimo = nos_atuais[0]
    gerar_nos_perigosos(obs)

    #-------------------------------------------------

    while len(nos_atuais) > 0:
        bola = tem_bola
        nos_atuais.sort(key=lambda c: c.custo_atual)
        caminho_otimo = nos_atuais[0] 

        if caminho_otimo.testar_no_atual() == pos_objetivo: 
            break 

        caminho_otimo.add_proximos_nos(nos_atuais, nos_proibidos, x_objetivo, y_objetivo,x_max,y_max)
    

    if not nos_atuais: 
        return []
    return caminho_otimo.caminho_atual

