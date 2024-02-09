
from Prado_MT import eh_predador, eh_presa, obter_pos_x, obter_pos_y, obter_posicoes_adjacentes, obter_tamanho_x, obter_tamanho_y, cria_posicao, cria_animal, cria_prado, posicao_para_str, eh_posicao


def prado_para_str(m):
    """prado para str(m) devolve uma cadeia de caracteres que representa o prado como mostrado nos exemplos."""
    #for x in obter_tamanho_x(m):
        #if eh_animal return @
        #if eh_posicao_livre return .
        #if eh_posicao_obstaculo return |
    #for y in obter_tamanho_y(m):
        #if eh_animal return @
        #if eh_posicao_livre return .
        #if eh_posicao_obstaculo return |
    return '+-------------+\n|p.p@.........|\n|.G...........|\n|@...p....@...|\n+-------------+\n'


def obter_valor_numerico(m, p):
    """obter valor numerico(m, p) devolve o valor numerico da posicao p correspondente a ordem de leitura no prado m."""
    xsize = obter_tamanho_x(m) - 1
    y = obter_pos_y(p) + 1
    res = (xsize*y + obter_pos_y(p)) - (xsize-obter_pos_x(p))
    return res

#def obter_movimento(m, p):
   # """obter movimento(m, p) devolve a posicao seguinte do animal na posicao p dentro do prado m de acordo com as regras de movimento dos animais no prado."""
   # if eh_presa(p):
  #     obter_posicoes_adjacentes(p)
   # else:
    #    if obter_posicoes_adjacentes(p)
   #return


def obter_posicoes_adjacentes(p):
    """obter posicoes adjacentes(p) devolve um tuplo com as posicoes adjacentes a posicao p, comecando pela posicao 
    acima de p e seguindo no sentido horario."""
    if eh_posicao and (obter_pos_x(p)-1) >= 0 and (obter_pos_y(p)-1) >= 0: # se as coordenadas forem diferentes de 0
        return ((obter_pos_x(p))-1, obter_pos_y(p)),(obter_pos_x(p)+1, obter_pos_y(p)),(((obter_pos_x(p),obter_pos_y(p)-1))),(((obter_pos_x(p), obter_pos_y(p)+1)))
    elif obter_pos_x(p) == 0: #se a coordenada x for 0
        return((obter_pos_x(p)+1), obter_pos_y(p)),(((obter_pos_x(p), obter_pos_y(p)+1)))
    elif obter_pos_y(p) == 0: #se a coordenada y for 0
        return((obter_pos_x(p)-1), obter_pos_y(p)),((obter_pos_x(p)+1), obter_pos_y(p)),((obter_pos_x(p), obter_pos_y(p)+1))
    else: #se ambas as coordenadas x e y forem 0
        return((obter_pos_x(p)+1),(obter_pos_y(p))),((obter_pos_x(p), obter_pos_y(p)+1))

dim = cria_posicao(11, 4)
obs = (cria_posicao(4,2), cria_posicao(5,2))
an1 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an2 = (cria_animal('lynx', 20, 15),)
pos = tuple(cria_posicao(p[0],p[1]) \
                        for p in ((5,1),(7,2),(10,1),(6,1)))
prado = cria_prado(dim, obs, an1+an2, pos)



