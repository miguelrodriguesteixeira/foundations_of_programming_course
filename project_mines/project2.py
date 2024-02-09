#------------------------------------------------------------------------------------------------------#
# Fundamentos da Programacao - 2022/2023
# Segundo Projeto - Minas
# Miguel Teixeira - ist1103449
#------------------------------------------------------------------------------------------------------#
#  TAD gerador
#------------------------------------------------------------------------------------------------------#

# Construtores
def cria_gerador(b, s):
    """cria gerador(b, s) recebe um inteiro b correspondente ao numero de bits do gerador e um 
    inteiro positivo s correspondente a seed ou estado inicial, e devolve o gerador correspondente."""
    if type(b) != int or type(s) != int or s <= 0:
        raise ValueError('cria_gerador: argumentos invalidos')
    if not (b == 32) and not (b == 64): # o numero de bits tem que ser 32 ou 64
        raise ValueError('cria_gerador: argumentos invalidos')
    if b == 32: # a seed tem um limite de 2^32 para 32 bits
        if (2**32) < s: 
            raise ValueError('cria_gerador: argumentos invalidos')
    if b == 64: # a seed tem um limite de 2^64 para 64 bits
        if (2**64) < s:
            raise ValueError('cria_gerador: argumentos invalidos')
    return [b,s]

def cria_copia_gerador(g):
    """cria copia gerador(g) recebe um gerador e devolve uma copia nova do gerador."""
    return cria_gerador(g[0], g[1])

# Selectores
def obtem_bits(g):
    return g[0] # funcao auxiliar para obter os bits

def obtem_estado(g):
    """obtem estado(g) devolve o estado atual do gerador g sem o alterar."""
    return g[1]

# Modificadores
def define_estado(g,s):
    """define estado(g, s) define o novo valor do estado do gerador g como sendo s,
    e devolve s."""
    g.remove(g[1])
    g.insert(1,s)
    return g[1]

def atualiza_estado(g):
    """atualiza estado(g) atualiza o estado do gerador g de acordo com o 
    algoritmo xorshift de geracao de numeros pseudoaleatorios, e devolve-o."""
    a = g[0]
    b = g[1]
    g.remove(g[0])
    g.remove(g[0])
    if a == 32:
        b ^= ( b << 13 ) & 0xFFFFFFFF
        b ^= ( b >> 17 ) & 0xFFFFFFFF
        b ^= ( b << 5 ) & 0xFFFFFFFF
    else:
        b ^= ( b << 13 ) & 0xFFFFFFFFFFFFFFFF
        b ^= ( b >> 7 ) & 0xFFFFFFFFFFFFFFFF
        b ^= ( b << 17 ) & 0xFFFFFFFFFFFFFFFF
    g.insert(0, a)
    g.insert(1, b)
    return g[1]

# Reconhecedor
def eh_gerador(arg):
    """eh gerador(arg) devolve True caso o seu argumento seja um TAD gerador e False caso contrario."""
    if not(type(arg) == list and len(arg) == 2):
        return False
    if type(arg[0]) != int or type(arg[1]) != int or arg[1] <= 0:
        return False
    if not (arg[0] == 32) and not (arg[0] == 64): # o numero de bits tem que ser 32 ou 64
        return False
    if arg[0] == 32: # a seed tem um limite de 2^32 para 32 bits
        if (2**32) < arg[1]: 
            return False
        else:
            return True
    if arg[0] == 64: # a seed tem um limite de 2^64 para 64 bits
        if (2**64) < arg[1]:
            return False
        else:
            return True

# Teste
def geradores_iguais(g1,g2):
    """geradores iguais(g1, g2) devolve True apenas se g1 e g2 sao geradores e sao iguais."""
    return eh_gerador(g1) and eh_gerador(g2) and obtem_estado(g1) == obtem_estado(g2) and obtem_bits(g1) == obtem_bits(g2)

# Transformador
def gerador_para_str(g):
    """gerador para str(g) devolve a cadeia de carateres que representa o seu argumento."""
    return 'xorshift{}(s={})'.format(g[0],g[1])

# Alto nivel
def gera_numero_aleatorio(g,n):
    """gera numero aleatorio(g, n) atualiza o estado do gerador g e devolve um numero 
    aleatorio no intervalo [1, n]"""
    s = atualiza_estado(g)
    numero = 1 + s % n
    return numero

def gera_carater_aleatorio(g,c):
    """gera carater aleatorio(g, c) atualiza o estado do gerador g e devolve um carater aleatorio 
    no intervalo entre 'A' e o carater maiusculo c. Este e obtido a partir do novo estado s de g 
    como o carater na posicao mod(s, l) da cadeia de carateres de tamanho l formada por todos os 
    carateres entre 'A' e c."""
    s = atualiza_estado(g)
    l = (ord(c) - ord('A')) + 1
    inicial = ord('A')
    carater = s % l
    carater += inicial
    return chr(carater)

#------------------------------------------------------------------------------------------------------#
#  TAD coordenada
#------------------------------------------------------------------------------------------------------#

# Construtor
def cria_coordenada(col, lin):
    """cria coordenada(col, lin) recebe os valores correspondentes a coluna col e linha lin 
    e devolve a coordenada correspondente. O construtor verifica a validade dos seus argumentos."""
    if type(col) != str or type(lin) != int or len(col) != 1:
        raise ValueError('cria_coordenada: argumentos invalidos')
    if (ord('A') > ord(col)) or (ord('Z') < ord(col)):
        raise ValueError('cria_coordenada: argumentos invalidos')
    if lin < 1 or lin > 99:
        raise ValueError('cria_coordenada: argumentos invalidos')
    return ((col,lin))

# Seletores
def obtem_coluna(c):
    """obtem coluna(c) devolve a coluna col da coordenada c."""
    return c[0]

def obtem_linha(c):
    """obtem linha(c) devolve a linha lin da coordenada c."""
    return c[1]

# Reconhecedor
def eh_coordenada(arg):
    """eh coordenada(arg) devolve True caso o seu argumento seja um TAD coordenada e False caso contrario."""
    if not(type(arg) == tuple and len(arg) == 2):
        return False
    if type(arg[0]) != str or type(arg[1]) != int or len(arg[0]) != 1:
        return False
    if (ord('A') > ord(arg[0])) or (ord('Z') < ord(arg[0])):
        return False
    if arg[1] < 1 or arg[1] > 99:
        return False
    return True

# Teste
def coordenadas_iguais(c1,c2):
    """coordenadas iguais(c1, c2) devolve True apenas se c1 e c2 sao coordenadas e sao iguais."""
    return eh_coordenada(c1) and eh_coordenada(c2) and obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2)

# Transformador
def coordenada_para_str(c):
    """coordenada para str(c) devolve a cadeia de carateres que representa o seu argumento."""
    if c[1] < 10:
        return '{}0{}'.format(c[0],c[1])
    return '{}{}'.format(c[0],c[1])

def str_para_coordenada(s):
    """str para coordenada(s) devolve a coordenada reapresentada pelo seu argumento."""
    if s[1] == '0':
        return ((s[0], int(s[2])))
    return ((s[0],int(s[1:3])))

# Alto nivel
def obtem_coordenadas_vizinhas(c):
    """obtem coordenadas vizinhas(c) devolve um tuplo com as coordenadas vizinhas da coordenada c, 
    comecando pela coordenada na diagonal acima-esquerda de c e seguindo no sentido horario."""
    viz = ()
    lin_og = obtem_linha(c)
    col_og = obtem_coluna(c)

    if lin_og == 1: # coordenada de linha um
        if col_og == 'A': # coordenada de coluna A
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
        elif col_og == 'Z': # coordenada de coluna Z
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og),
        else:
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og+1),
            

    elif lin_og == 99: # coordenada de linha 99
        if col_og == 'A': # coordenada de coluna A
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
        elif col_og == 'Z': # coordenada de coluna Z
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og), 
        else: 
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og),
    
    else:
        if col_og == 'A': # coordenada de coluna A
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
        elif col_og == 'Z': # coordenada de coluna Z
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og),
        else: 
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og-1),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og),
            viz += cria_coordenada((chr(ord(col_og)+1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og))), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og+1),
            viz += cria_coordenada((chr(ord(col_og)-1)), lin_og),
    return viz

def obtem_coordenada_aleatoria(c,g):
    """obtem coordenada aleatoria(c, g) recebe uma coordenada c e um TAD gerador g, e devolve uma 
    coordenada gerada aleatoriamente em que c define a maior coluna e maior linha possiveis."""
    col = obtem_coluna(c)
    lin = obtem_linha(c)
    car_aleatorio = gera_carater_aleatorio(g, col)
    num_aleatorio = gera_numero_aleatorio(g,lin)
    return cria_coordenada(car_aleatorio,num_aleatorio)

#------------------------------------------------------------------------------------------------------#
#  TAD parcela
#------------------------------------------------------------------------------------------------------#

# Construtor
def cria_parcela():
    """cria parcela() devolve uma parcela tapada sem mina escondida.""" 
    return [chr(35),False] # parcela tapada '#'

def cria_copia_parcela(p):
    """cria copia parcela(p) recebe uma parcela p e devolve uma nova copia da parcela."""
    return [p[0],p[1]]

# Modificadores
def limpa_parcela(p):
    """limpa parcela(p) modifica destrutivamente a parcela p modificando o seu 
    estado para limpa, e devolve a propria parcela."""
    f = chr(63) # parcelas limpas sem mina '?'
    s = chr(88) # parcelas limpas com mina 'X'
    if p[1] == False: # nao tem mina
        p.remove(p[0])
        p.insert(0, f)
        return p
    else: # tem mina
        p.remove(p[0])
        p.insert(0, s)
        return p

def marca_parcela(p):
    """marca parcela(p) modifica destrutivamente a parcela p modificando o seu 
    estado para marcada com uma bandeira, e devolve a propria parcela."""
    f = chr(64) # parcela marcada '@'
    p.remove(p[0])
    p.insert(0, f)
    return p

def desmarca_parcela(p):
    """desmarca parcela(p) modifica destrutivamente a parcela p modificando o seu 
    estado para tapada, e devolve a propria parcela."""
    f = chr(35) # desmarcada '#'
    p.remove(p[0])
    p.insert(0, f)
    return p

def esconde_mina(p):
    """esconde mina(p) modifica destrutivamente a parcela p escondendo uma mina
    na parcela, e devolve a propria parcela."""
    if eh_parcela_limpa(p):
        f = chr(88)
    else:
        f = p[0]
    s = True
    p.remove(p[0])
    p.remove(p[0])
    p.insert(0, f)
    p.insert(1, s)
    return p

# Reconhecedor
def eh_parcela(arg):
    """eh parcela(arg) devolve True caso o seu argumento seja um TAD parcela e
    False caso contrario."""
    if (type(arg) != list) or (len(arg) != 2):
        return False
    if not (arg[0] == chr(63)) and not (arg[0] == chr(35)) and not (arg[0] == chr(64)) and not (arg[0] == chr(88)) and not(arg[0].isnumeic()):
        return False
    if not (arg[1] == True) and not (arg[1] == False):
        return False
    return True

def eh_parcela_tapada(p):
    """eh parcela tapada(p) devolve True caso a parcela p se encontre tapada e False caso contrario."""
    return (p[0] == chr(35)) and eh_parcela(p)

def eh_parcela_marcada(p):
    """eh parcela marcada(p) devolve True caso a parcela p se encontre marcada
    com uma bandeira e False caso contrario."""
    return (p[0] == chr(64)) and eh_parcela(p)

def eh_parcela_limpa(p):
    """eh parcela limpa(p) devolve True caso a parcela p se encontre limpa e False caso contrario."""
    return (p[0] == chr(63) or p[0] == chr(88) or p[0].isnumeric()) and eh_parcela(p)

def eh_parcela_minada(p):
    """eh parcela minada(p) devolve True caso a parcela p esconda uma mina e
    False caso contrario."""
    return (p[1] == True) and eh_parcela(p)

# Teste
def parcelas_iguais(p1,p2):
    """parcelas iguais(p1, p2) devolve True apenas se p1 e p2 sao parcelas e sao
    iguais."""
    return eh_parcela(p1) and eh_parcela(p2) and (p1[0] == p2[0]) #sem contabilizar com as bombas

# Transformadores
def parcela_para_str(p):
    """parcela para str(p) devolve a cadeia de caracteres que representa a parcela em 
    funcao do seu estado: parcelas tapadas ('#'), parcelas marcadas ('@'), parcelas 
    limpas sem mina ('?') e parcelas limpas com mina ('X')."""
    s = ''.join(p[0])
    return s

# Alto nivel
def alterna_bandeira(p):
    """alterna bandeira(p) recebe uma parcela p e modifica-a destrutivamente da seguinte 
    forma: desmarca se estiver marcada e marca se estiver tapada, devolvendo True. 
    Em qualquer outro caso, nao modifica a parcela e devolve False."""
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    else:
        return False

#------------------------------------------------------------------------------------------------------#
#  TAD campo
#------------------------------------------------------------------------------------------------------#

# Funcoes auxiliares
def lista_letras(letra): # funcao auxiliar que lista as letras correspondentes a um campo
    lista = ()
    i = 'A'
    while ord(i) <= ord(letra):
        lista += (i,)
        i = chr(ord(i)+1)
    return lista

def lista_numeros(num): # funcao auxiliar que lista os numeros correspondentes a um campo
    lista = ()
    i = 1
    while i <= num:
        lista += '{}'.format(i),
        i += 1
    return lista

def lista_numeros2(num): # funcao auxiliar que lista os numeros correspondentes a um campo
    lista = () # segundo a representacao em string
    i = 1
    while i <= num:
        if i < 10:
            lista += '0''{}'.format(i), # se comecar com um 0 
            i += 1
        else:
            lista += '{}'.format(i), # se for maior que 9
            i += 1
    return lista

# Construtor
def cria_campo(c, l):
    """cria campo(c, l) recebe uma cadeia de carateres e um inteiro correspondentes a ultima 
    coluna e a ultima linha de um campo de minas, e devolve o campo do tamanho pretendido 
    formado por parcelas tapadas sem minas. O construtor verifica a validade dos seus argumentos."""
    if type(c) != str or type(l) != int or not eh_coordenada((c,l)):
        raise ValueError('cria_campo: argumentos invalidos')
    colunas = lista_letras(c)
    linhas = lista_numeros(l) 
    campo = {'coordenadas': [], 'parcelas': []} # fazer um dicionario
    for letra in colunas:
        for numero in range(len(linhas)): # e associar a cada chave(coordenada, parcela) os valores 
            campo['coordenadas'].append(cria_coordenada(letra, numero+1))
            campo['parcelas'].append(cria_parcela())
    return campo

def cria_copia_campo(m):
    """cria copia campo(m) recebe um campo e devolve uma nova copia do campo."""
    f = m['coordenadas']
    ult_coordenada = f[-1]
    ult_col = ult_coordenada[0]
    ult_lin = ult_coordenada[1]
    return cria_campo(ult_col, ult_lin)

# Seletores
def obtem_ultima_coluna(m):
    """obtem ultima coluna(m) devolve a cadeia de 
    caracteres que corresponde a ultima coluna do campo de minas."""
    lista_coordenadas = m['coordenadas']
    ult_coordenada = lista_coordenadas[-1]
    ult_col = ult_coordenada[0]
    return ult_col

def obtem_ultima_linha(m):
    """obtem ultima linha(m) devolve o valor inteiro que corresponde a ultima linha
    do campo de minas."""
    lista_coordenadas = m['coordenadas']
    ult_coordenada = lista_coordenadas[-1]
    ult_lin = ult_coordenada[1]
    return ult_lin

def obtem_parcela(m, c):
    """obtem parcela(m, c) devolve a parcela do campo m que se encontra na coordenada c."""
    aux = 0
    for i in m['coordenadas']:
        if i == c:
            parcela = m['parcelas'][aux]
            aux += 1
        else:
            aux += 1
    return parcela

def ordem_ascendente(tuplo): # funcao auxiliar para ordenar coordenadas
    aux = ()
    aux2 = ()
    resultado = ()
    aux = sorted(tuplo, key=lambda t: (t[1],t[0]))
    for coordenada in aux:
        aux2 += (coordenada_para_str(coordenada),)
    for elemento in aux2:
        resultado += (str_para_coordenada(elemento),)
    return tuple(resultado)

def obtem_coordenadas(m,s):
    """devolve o tuplo formado pelas coordenadas ordenadas em ordem ascendente de esquerda 
    a direita e de cima a baixo das parcelas dependendo do valor de s: 'limpas' para as parcelas 
    limpas, 'tapadas' para as parcelas tapadas, 'marcadas' para as parcelas marcadas, e 'minadas'
    para as parcelas que escondem minas"""
    resultado = ()
    aux = 0
    if s == 'limpas':
        for i in m['parcelas']:
            if eh_parcela_limpa(i):
                resultado += (m['coordenadas'][aux]),
                aux += 1
            else:
                aux += 1
        return ordem_ascendente(resultado)

    elif s == 'tapadas':
        for i in m['parcelas']:
            if eh_parcela_tapada(i):
                resultado += (m['coordenadas'][aux]),
                aux += 1
            else:
                aux += 1
        return ordem_ascendente(resultado)
    
    elif s == 'marcadas':
        for i in m['parcelas']:
            if eh_parcela_marcada(i):
                resultado += (m['coordenadas'][aux]),
                aux += 1
            else:
                aux += 1
        return ordem_ascendente(resultado)
    
    elif s == 'minadas':
        for i in m['parcelas']:
            if eh_parcela_minada(i):
                resultado += (m['coordenadas'][aux]),
                aux += 1
            else:
                aux += 1
        return ordem_ascendente(resultado)

def obtem_numero_minas_vizinhas(m, c):
    """devolve o numero de parcelas vizinhas
    da parcela na coordenada c que escondem uma mina"""
    contador = 0
    lista_viz = obtem_coordenadas_vizinhas(c)
    lista_minas = obtem_coordenadas(m, 'minadas')
    for viz in lista_viz:
        if viz in lista_minas:
            contador += 1
        else:
            continue
    return contador

# Reconhecedores
def eh_campo(arg):
    """eh campo(arg) devolve True caso o seu argumento seja um TAD campo e
    False caso contrario."""
    if (type(arg) != dict) or (list(arg.keys()) != ['coordenadas','parcelas']):
        return False
    if (len(arg['coordenadas']) <= 0) or (len(arg['parcelas']) <= 0):
        return False
    if (len(arg['coordenadas']) != len(arg['parcelas'])): # mesmo numero de coordenadas e parcelas
        return False
    for coordenada in arg['coordenadas']:
        if not eh_coordenada(coordenada):
            return False
        else:
            continue
    for parcela in arg['parcelas']:
        if not eh_parcela(parcela):
            return False
        else:
            continue
    return True

def eh_coordenada_do_campo(m,c):
    """eh coordenada do campo(m, c) devolve True se c e uma 
    coordenada valida dentro do campo m."""
    for coordenada in m['coordenadas']:
        if c in m['coordenadas']:
            return True
        else:
            continue
    return False

# Teste
def campos_iguais(m1,m2):
    """campos iguais(m1, m2) devolve True apenas se m1 e m2 forem campos e forem iguais."""
    return eh_campo(m1) and eh_campo(m2) and m1['coordenadas'] == m2['coordenadas']\
        and m1['parcelas'] == m2['parcelas']

# Transformador
def campo_para_str(m):
    """campo para str(m) devolve uma cadeia de caracteres que representa 
    o campo de minas."""
    ult_col = obtem_ultima_coluna(m)
    list_letras = lista_letras(ult_col)
    quant_letras = len(list_letras)
    list_letras2 = ''.join(list_letras)
    ult_lin = obtem_ultima_linha(m)
    list_numeros = lista_numeros2(ult_lin)
    quant_numeros = len(list_numeros)
    list_parcelas = lista_parcelas(m, list_letras)
    tamanho_total = quant_numeros*quant_letras
    lista_parcelas_final = list(list_parcelas)
    aux = ''
    nova_lista = []
    for l in range(quant_numeros):
        nova_lista += [lista_parcelas_final[l:tamanho_total:quant_numeros],]
    for i in range(ult_lin):
        aux += '\n{}|{}|'.format(list_numeros[i], ''.join(nova_lista[i]))
    aux += '\n  +'+ '-'*quant_letras + '+'
    aux2 = '\n  +'+ '-'*quant_letras + '+'
    string_campo = '   {}{}{}'.format(list_letras2, aux2, aux)

    return string_campo

def lista_parcelas(m, lista_letra): # funcao auxiliar que lista as parcelas correspondentes a um campo
    lista_res = ''
    aux = 0
    for i in m['coordenadas']:
        num_minas_viz = obtem_numero_minas_vizinhas(m, i)
        if eh_parcela_limpa(m['parcelas'][aux]) and not eh_parcela_minada(m['parcelas'][aux]):
            if num_minas_viz > 0:
                lista_res += '{}'.format(num_minas_viz)
                aux += 1
            else:
                lista_res += '{}'.format(' ')
                aux += 1
        else: 
            lista_res += parcela_para_str(m['parcelas'][aux])
            aux += 1
    return lista_res

# Alto nivel
def coloca_minas(m, c, g, n):
    """coloca minas(m, c, g, n) modifica destrutivamente o campo m escondendo n minas em parcelas 
    dentro do campo. As n coordenadas sao geradas em sequencia utilizando o gerador g, de modo a que 
    nao coincidam com a coordenada c nem com nenhuma parcela vizinha desta, nem se sobreponham com 
    minas colocadas anteriormente."""
    fim_campo = cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m))
    lista_vizinhas = obtem_coordenadas_vizinhas(c)
    numero_minas_a_colocar = 0
    lista_coordenadas = m['coordenadas']
    
    lista_viz_real = () # para ver as vizinhas de c no campo m
    for viz in lista_vizinhas:
        if eh_coordenada_do_campo(m, viz):
            lista_viz_real += (viz,)
        else:
            continue
    
    while numero_minas_a_colocar != n:
        coord_aleatoria = obtem_coordenada_aleatoria(fim_campo,g)
        lista_coordenadas_minas = obtem_coordenadas(m, 'minadas')
        if coord_aleatoria in lista_coordenadas_minas: # se sobrepoe com minas colocadas anteriormente
            continue
        elif (coord_aleatoria in lista_viz_real) or (coord_aleatoria == c): # se sao vizinhas de c ou e c
            continue
        else: # adicionar a mina na posicao aleatoria
            for i in range(len(lista_coordenadas)):
                if (m['coordenadas'][i] == coord_aleatoria) and (eh_coordenada_do_campo(m, coord_aleatoria)):
                    esconde_mina(m['parcelas'][i])
                    numero_minas_a_colocar += 1
                else:
                    continue
    return m


def limpa_campo(m, c):
    """limpa campo(m, c) modifica destrutivamente o campo limpando a parcela na coordenada c, devolvendo-o. 
    Se nao houver nenhuma mina vizinha escondida, limpa iterativamente todas as parcelas vizinhas. 
    Caso a parcela se encontre ja limpa, a operacao nao tem efeito."""
    lista_coordenadas = m['coordenadas']

    if eh_parcela_limpa(obtem_parcela(m,c)): # a parcela ja se encontra limpa
        return m # a operacao nao tem efeito
    
    lista_viz = obtem_coordenadas_vizinhas(c) # coordenadas vizinhas de c
    
    lista_viz_real = () # para ver as vizinhas de c no campo m
    for v in lista_viz:
        if eh_coordenada_do_campo(m, v):
            lista_viz_real += (v,)
        else:
            continue
    
    lista_viz_minas = () # para ver as vizinhas minas de c no campo m
    for viz in lista_viz_real:
        if eh_parcela_minada(obtem_parcela(m, viz)):
            lista_viz_minas += viz
        else:
            continue
    
    for i in range(len(lista_coordenadas)): # limpa a parcela na coordenada c e devolve-a
        if (m['coordenadas'][i]) == c:
            limpa_parcela(m['parcelas'][i])
        else:
            continue

    if lista_viz_minas == () and not eh_parcela_minada(obtem_parcela(m,c)): # se nao houver nenhuma mina vizinha escondida
        for parcela_vizinha in lista_viz_real: # limpa iterativamente todas as parcelas vizinhas
            limpa_campo(m, parcela_vizinha)  
 
    return m

#------------------------------------------------------------------------------------------------------#
# Funcoes adicionais
#------------------------------------------------------------------------------------------------------#

def jogo_ganho(m):
    """jogo ganho(m) e uma funcao auxiliar que recebe um campo do jogo das minas e devolve
    True se todas as parcelas sem minas se encontram limpas, ou False caso contrario."""
    lista_limpas = obtem_coordenadas(m, 'limpas')
    lista_minadas = obtem_coordenadas(m, 'minadas')
    lista_coordenadas = m['coordenadas']
    num_coordenadas = len(lista_coordenadas)
    if num_coordenadas == len(lista_limpas) + len(lista_minadas):
        return True
    else:
        return False

def turno_jogador(m):
    """turno jogador(m) e uma funcao auxiliar que recebe um campo de minas e oferece ao jogador a 
    opcao de escolher uma acao e uma coordenada. A funcao modifica destrutivamente
    o campo de acordo com a acao escolhida, devolvendo False caso o jogador tenha limpo
    uma parcela que continha uma mina, ou True caso contrario."""
    comando = input('Escolha uma ação, [L]impar ou [M]arcar:')
    
    if comando == chr(76): # escolha L
        coordenada = input('Escolha uma coordenada:')
        while not (eh_coordenada_str(coordenada,m)):
            coordenada = input('Escolha uma coordenada:')
        s = str_para_coordenada(coordenada)
        if eh_parcela_minada(obtem_parcela(m, s)):
            limpa_parcela(obtem_parcela(m, s))
            return False
        else:
            limpa_campo(m,s)
        return True

    elif comando == chr(77): # escolha M
        coordenada = input('Escolha uma coordenada:')
        while not (eh_coordenada_str(coordenada,m)):
            coordenada = input('Escolha uma coordenada:')
        s = str_para_coordenada(coordenada)
        marca_parcela(obtem_parcela(m, s))
        return True

    else: # acao invalida
        return turno_jogador(m)

def eh_coordenada_str(arg, m): # funcao auxiliar para ver se e coordenada
    # em formato string
    if len(arg) != 3: # se tiver menos que tres elementos
        return False
    else:
        if (type(arg[0]) != str):
            return False
        if (ord('A') > ord(arg[0])) or (ord('Z') < ord(arg[0])):
            return False
        if not (arg[1].isnumeric()) or not (arg[2].isnumeric()):
            return False
        if (int(arg[1]) == 0):
            if (int(arg[2]) < 1 or int(arg[2]) > 9):
                return False
        s = str_para_coordenada(arg)
        if not (eh_coordenada_do_campo(m, s)):
            return False
    return True


def minas(c, l, n, d, s):
    """minas(c, l, n, d, s) e a funcao principal que permite jogar ao jogo das minas. A funcao
    recebe uma cadeia de carateres e 4 valores inteiros correspondentes, respetivamente, a:
    ultima coluna c; ultima linha l; numero de parcelas com minas n; dimensao do gerador
    de numeros d; e estado inicial ou seed s para a geracao de numeros aleatorios. A funcao
    devolve True se o jogador conseguir ganhar o jogo, ou False caso contrario."""
    if (type(c)!=str) or (type(l)!=int) or (type(n)!=int) or (type(d)!=int) or (type(s)!=int):
        raise ValueError("minas: argumentos invalidos")
    if ('A' > c or c < 'Z') or (l < 1 or l > 99):
        raise ValueError("minas: argumentos invalidos")
    if not (d == 32) and not (d == 64):
        raise ValueError("minas: argumentos invalidos")

    m = cria_campo(c,l)
    g = cria_gerador(d, s)
    c_random = obtem_coordenada_aleatoria(cria_coordenada(c,l),g)
    m = coloca_minas(m,c_random,g,n)
    njogadas = 0

    while not jogo_ganho(m):
        #band_usadas = 0
        band_usadas = len(obtem_coordenadas(m, 'marcadas'))
        for f in m['parcelas']:
            if (band_usadas == n): # se atingir o numero maximo de bandeiras
                if jogo_ganho(m):
                    print('VITORIA!!!')
                    return True
                if not jogo_ganho(m):
                    print('BOOOOOOOM!!!')
                    return False
            #if eh_parcela_marcada(f):
                #band_usadas += 1 
        band_usadas = len(obtem_coordenadas(m, 'marcadas'))
        s = '   [Bandeiras {}/{}]\n'.format(band_usadas,n) + campo_para_str(m) #[Bandeiras 0/6]
        print(s)
        
        while njogadas == 0: # jogada inicial comeca por limpar coordenada inserida
            njogadas += 1
            turno_jogador_inicial(m)
            s = '   [Bandeiras {}/{}]\n'.format(band_usadas,n) + campo_para_str(m) #[Bandeiras 0/6]
            print(s)

        else:
            turno_jogador(m)

    if jogo_ganho(m):
        band_usadas = len(obtem_coordenadas(m, 'marcadas'))
        s = '   [Bandeiras {}/{}]\n'.format(band_usadas,n) + campo_para_str(m) #[Bandeiras 0/6]
        print(s)
        print('VITORIA!!!')
        return True

    if not turno_jogador(m):
        band_usadas = len(obtem_coordenadas(m, 'marcadas'))
        s = '   [Bandeiras {}/{}]\n'.format(band_usadas,n) + campo_para_str(m) #[Bandeiras 0/6]
        print(s)
        print('BOOOOOOOM!!!')
        return False

def turno_jogador_inicial(m): # funcao auxiliar para iniciar minas com pedido de coordenada
        coordenada = input('Escolha uma coordenada:')
        while not (eh_coordenada_str(coordenada,m)):
            coordenada = input('Escolha uma coordenada:')
        s = str_para_coordenada(coordenada)
        if eh_parcela_minada(obtem_parcela(m, s)):
            limpa_parcela(obtem_parcela(m, s))
            return False
        else:
            limpa_campo(m,s)
            return True

#------------------------------------------------------------------------------------------------------#
# FIM
#------------------------------------------------------------------------------------------------------# 
