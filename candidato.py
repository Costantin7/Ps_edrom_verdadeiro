# NOME DO CANDIDATO: Gabriel Freitas Costantin
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Estruturas e Movimento

import math

def func_custo(x_analisado, y_analisado, x_objetivo, y_objetivo):

    custo_distancia = math.sqrt( math.pow(x_analisado - x_objetivo,2) + math.pow(y_analisado - y_objetivo,2))
    custo_movimento = 0
    custo_proximidade_obstaculo = 0
    custo = custo_distancia + custo_movimento + custo_proximidade_obstaculo
    return custo

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):

    


    caminho_exemplo = []
    x_atual, y_atual = pos_inicial

 
            

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
