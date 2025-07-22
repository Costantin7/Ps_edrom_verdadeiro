# NOME DO CANDIDATO: Gabriel Freitas Costantin
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Estruturas e Movimento

import math


nivel1=1
nivel2=1
nivel3=1


# array de classes (2)
nos_atuais = []

# array de tuplas (3)
nos_proibidos = []

# Classe de nós 
class No_Atual:
    def __init__(self,x_atual,y_atual,caminho_atual,custo_atual):
        self.x_atual = x_atual
        self.y_atual = y_atual
        self.caminho_atual = caminho_atual
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
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,1))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

        if((self.x_atual , self.y_atual + 1) not in nos_proibidos and self.x_atual  <= x_max and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual 
            y_temporario = self.y_atual + 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,3))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))


        if((self.x_atual - 1 , self.y_atual ) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual <= y_max ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual 
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,5))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))


        if((self.x_atual  , self.y_atual - 1) not in nos_proibidos and self.x_atual  <= x_max and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual 
            y_temporario = self.y_atual - 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,7))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))
        

        if((self.x_atual + 1, self.y_atual + 1) not in nos_proibidos and self.x_atual + 1 < x_max and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual + 1
            y_temporario = self.y_atual + 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,2))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))

    
    

        if((self.x_atual - 1 , self.y_atual + 1) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual + 1 < y_max ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual + 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,4))
            caminho_temporario = self.caminho_atual.copy()
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))



        if((self.x_atual - 1 , self.y_atual - 1) not in nos_proibidos and self.x_atual - 1 >= 0 and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual - 1
            y_temporario = self.y_atual - 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,6))
            caminho_temporario = self.caminho_atual.copy()           
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))


        if((self.x_atual + 1  , self.y_atual - 1) not in nos_proibidos and self.x_atual + 1 < x_max and self.y_atual - 1 >= 0 ):
            x_temporario = self.x_atual + 1
            y_temporario = self.y_atual - 1
            custo_temporario = self.custo_atual + func_calcular_custo(x_temporario, y_temporario, x_objetivo, y_objetivo, func_mudou_direção(self.caminho_atual,8))
            caminho_temporario = self.caminho_atual.copy()         
            No_temporario = No_Atual(x_temporario,y_temporario,caminho_temporario,custo_temporario)
            No_temporario.add_no_atual()
            nos_proibidos.append((x_temporario,y_temporario))
                
        nos_atuais.remove(self)

# Essa função serve para calcular os pesos 
def func_calcular_custo(x_analisado, y_analisado, x_objetivo, y_objetivo, mudanca):

    #Parametros para ajuste fino

    linha_reta = 0
    diagonal = 0.4
    graus90 = 0.8
    antidiagonal = 1.2
    graus180 = 1.4 



    custo_distancia = math.sqrt( math.pow(x_analisado - x_objetivo,2) + math.pow(y_analisado - y_objetivo,2))
    custo_proximidade_obstaculo = 0

    
    if(mudanca == 0):# linha reta
        custo_movimento = linha_reta

    
    elif(mudanca == 1 or mudanca == 7):# linha diagonal proxima
        custo_movimento = diagonal
   
    elif(mudanca == 2 or mudanca == 6):# 90 gruas
        custo_movimento = graus90

    elif(mudanca == 3 or mudanca == 5):# anti diagonal 
        custo_movimento = antidiagonal

    elif(mudanca == 4): # 180
        custo_movimento = graus180




    custo = custo_distancia + custo_movimento + custo_proximidade_obstaculo
    return custo


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

    











# ==============================================================================================================
# Função principal
def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
 

    #setup -------------------------------------------------
    nos_atuais.clear()
    nos_proibidos.clear()

    x_max = largura_grid
    y_max = altura_grid
    x_inicial, y_inicial = pos_inicial
    x_objetivo , y_objetivo = pos_objetivo
    nos_proibidos.extend(obstaculos)
    caminho_inicial = []
    No = No_Atual (x_inicial, y_inicial,caminho_inicial,0)
    No.add_no_atual()
    nos_atuais.sort(key=lambda c: c.custo_atual)
    caminho_otimo = nos_atuais[0]


    #-------------------------------------------------

    while len(nos_atuais) > 0:
        nos_atuais.sort(key=lambda c: c.custo_atual)
        caminho_otimo = nos_atuais[0] 

        
        if caminho_otimo.testar_no_atual() == pos_objetivo: 
            break 


        caminho_otimo.add_proximos_nos(nos_atuais, nos_proibidos, x_objetivo, y_objetivo,x_max,y_max)
    



    if not nos_atuais: # Se a lista estiver vazia, não achou caminho
        return []
    return caminho_otimo.caminho_atual


    # Args:
    #     pos_inicial (tuple): A posição (x, y) inicial do robô.
    #     pos_objetivo (tuple): A posição (x, y) do objetivo (bola ou gol).
    #     obstaculos (list): Uma lista de tuplas (x, y) com as posições dos obstáculos.
    #     largura_grid (int): A largura do campo em células.
    #     altura_grid (int): A altura do campo em células.
    #     tem_bola (bool): Um booleano que indica o estado do robô.
    #                      True se o robô está com a bola, False caso contrário.
    #                      Este parâmetro é essencial para o Nível 2 do desafio.

    # Returns:
    #     list: Uma lista de tuplas (x, y) representando o caminho do início ao fim.
    #           A lista deve começar com o próximo passo após a pos_inicial e terminar
    #           na pos_objetivo. Se nenhum caminho for encontrado, retorna uma lista vazia.
    #           Exemplo de retorno: [(1, 2), (1, 3), (2, 3)]

    # caminhos_testados.sort(key=lambda c: c.custo_atual)
    #nos_proibidos.append(obstaculos)