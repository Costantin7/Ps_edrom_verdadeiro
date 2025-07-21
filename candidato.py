# NOME DO CANDIDATO: Gabriel Freitas Costantin
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Estruturas e Movimento

import math

nos_encontrados = []

nos_proibidos = []

 
# Classe de nós 
class No_Atual:
    def __init__(self):
        self.x_atual = 0
        self.y_atual = 0
        self.caminho_atual = []
        self.custo_atual = 0
        self.finalizado = False

    def primeiro_caminho(self, x_inicial, y_inicial): 
        self.x_atual = x_inicial
        self.y_atual = y_inicial
        self.caminho_atual.append((x_inicial,y_inicial))
        nos_encontrados.append(self)

    def add_proximos_nos(self,nos_encontrados,nos_proibidos):
        nos_encontrados.remove(self)
        
   


# Essa função serve para calcular os pesos 
def func_calcular_custo(x_analisado, y_analisado, x_objetivo, y_objetivo):

    custo_distancia = math.sqrt( math.pow(x_analisado - x_objetivo,2) + math.pow(y_analisado - y_objetivo,2))
    custo_movimento = 0
    custo_proximidade_obstaculo = 0
    custo = custo_distancia + custo_movimento + custo_proximidade_obstaculo
    return custo






# ==============================================================================================================
# Função principal
def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):


    #setup -------------------------------------------------

    x_inicial, y_inicial = pos_inicial
    # ADD obstaculos a nós poribidos 
    nos_proibidos.append(obstaculos)
    No = No_Atual
    No.primeiro_caminho(x_inicial, y_inicial)

    #-------------------------------------------------

 



    # caminho_exemplo.append((proximo_x, y_atual))
    return caminho_exemplo


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