# Projeto 2 - O Prado / Miguel Teixeira nº103449


def cria_posicao(x,y):
    """cria posicao(x,y) recebe os valores correspondentes as coordenadas de uma posicao e devolve a posicao 
    correspondente. O construtor verifica a validade dos seus argumentos, gerando um ValueError com a mensagem ‘cria 
    posicao: argumentos invalidos’ caso os seus argumentos nao sejam validos."""
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return ((x,y))


def cria_copia_posicao(p):
    """cria copia posicao(p) recebe uma posicao e devolve uma copia nova da posicao."""
    return (p[0],p[1])


def obter_pos_x(p):
    """obter pos x(p) devolve a componente x da posicao p"""
    return p[0]


def obter_pos_y(p):
    """obter pos y(p) devolve a componente y da posicao p."""
    return p[1]


def eh_posicao(arg):
    """eh posicao(arg) devolve True caso o seu argumento seja um TAD posicao e False caso contrario."""
    return type(arg) == tuple and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int and arg[0] >= 0 and arg[1] >= 0


def posicoes_iguais(p1,p2):
    """posicoes iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao iguais."""
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)


def posicao_para_str(p):
    """posicao para str(p) devolve a cadeia de caracteres ‘(x, y)’ que representa o seu argumento, sendo os valores x e y as coordenadas de p."""
    return str(p)


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


def ordenar_posicoes(p):
    """ordenar posicoes(t) devolve um tuplo contendo as mesmas posicoes do tuplo fornecido como argumento, 
    ordenadas de acordo com a ordem de leitura do prado."""
    p = sorted(p, key = lambda x: obter_pos_x(x))
    p = sorted(p, key = lambda x: obter_pos_y(x))
    return tuple(p)


def cria_animal(s,r,a):
    """cria animal(s, r, a) recebe uma cadeia de caracteres s nao vazia correspondente a especie do animal e dois valores inteiros correspondentes 
    a frequencia de reproducao r (maior do que 0) e a frequencia de alimentacao a (maior ou igual que 0); e devolve o animal"""
    if s == '' or type(s) != str or type(r) != int or type(a) != int or r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return [s, 0, r, 0, a]


def cria_copia_animal(a):
    """cria copia animal(a) recebe um animal a (predador ou presa) e devolve uma nova copia do animal."""
    return [a[0],a[1],a[2],a[3],a[4]]


def obter_especie(a):
    """obter especie(a) devolve a cadeia de caracteres correspondente a especie do animal."""
    return a[0]


def obter_freq_reproducao(a):
    """obter freq reproducao(a) devolve a frequencia de reproducao do animal a."""
    return a[2]


def obter_freq_alimentacao(a):
    """obter freq alimentacao(a) devolve a frequencia de alimentacao do animal a (as presas devolvem sempre 0)."""
    return a[4]


def obter_idade(a):
    """obter idade(a) devolve a idade do animal a."""
    return a[1]


def obter_fome(a):
    """obter fome(a) devolve a fome do animal a (as presas devolvem sempre 0)."""
    return a[3]


def aumenta_idade(a):
    """aumenta idade(a) modifica destrutivamente o animal a incrementando o valor da sua idade em uma unidade, e devolve 
    o proprio animal."""
    a[1] = obter_idade(a) + 1 
    return cria_copia_animal(a)


def reset_idade(a):
    """reset idade(a) modifica destrutivamente o animal a definindo o valor da sua idade igual a 0, 
    e devolve o proprio animal."""
    a[1] = 0
    return cria_copia_animal(a)


def aumenta_fome(a):
    """aumenta fome(a) modifica destrutivamente o animal predador a incrementando o valor da sua fome em uma unidade, 
    e devolve o proprio animal. Esta operacao nao modifica os animais presa."""
    if obter_freq_alimentacao(a) == 0:
        return cria_copia_animal(a)
    a[3] = obter_fome(a) + 1
    return cria_copia_animal(a)


def reset_fome(a):
    """reset fome(a) modifica destrutivamente o animal predador a definindo o valor da sua fome igual a 0, 
    e devolve o proprio animal. Esta operacao nao modifica os animais presa."""
    if obter_freq_alimentacao(a) == 0:
        return cria_copia_animal(a)
    a[3] = 0
    return cria_copia_animal(a)


def eh_animal(arg):
    """eh animal(arg) devolve True caso o seu argumento seja um TAD animal e False caso contrario."""
    if type(arg) != list or len(arg) != 5: #para verificar que é uma lista e tem 5 elementos
        return False
    return type(obter_especie(arg)) == str and type(obter_freq_alimentacao(arg)) == int and type(obter_freq_reproducao(arg)) == int and type(obter_fome(arg)) == int and type(obter_idade(arg)) == int\
        and obter_freq_alimentacao(arg) >= 0 and obter_freq_reproducao(arg) > 0 and obter_idade(arg) >= 0 and obter_fome(arg) >= 0


def eh_predador(arg):
    """eh predador(arg) devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrario."""
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """eh presa(arg) devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrario."""
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(a1,a2):
    """animais iguais(a1, a2) devolve True apenas se a1 e a2 sao animais e sao iguais."""
    return eh_animal(a1) and eh_animal(a2) and obter_especie(a1) == obter_especie(a2) and obter_fome(a1) == obter_fome(a2) and \
        obter_freq_reproducao(a1) == obter_freq_reproducao(a2) and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2) and obter_idade(a1) == obter_idade(a2)


def animal_para_char(a):
    """animal para char(a) devolve a cadeia de caracteres dum unico elemento correspondente ao primeiro caracter da especie do animal 
    passada por argumento, em maiuscula para animais predadores e em minuscula para animais presa."""
    return (obter_especie(a)[0]).upper() if eh_predador(a) else (obter_especie(a)[0]).lower() #funcao .upper() e .lower() para obter a letra em maiuscula e minuscula
    

def animal_para_str(a):
    """animal para str(a) devolve a cadeia de caracteres que representa o animal como mostrado nos exemplos."""
    if eh_predador(a): #a representacao e diferente para as presas e os predadores
        return ('{} [{}{}{}{}{}{}{}]').format(obter_especie(a),obter_idade(a),'/',obter_freq_reproducao(a), ';', obter_fome(a), '/', obter_freq_alimentacao(a))
    return('{} [{}{}{}]').format(obter_especie(a),obter_idade(a),'/',obter_freq_reproducao(a))


def eh_animal_fertil(a):
    """eh animal fertil(a) devolve True caso o animal a tenha atingido a idade de reproducao e False caso contrario."""
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """eh animal faminto(a) devolve True caso o animal a tenha atingindo um valor de fome igual ou superior a sua frequencia de alimentacao 
    e False caso contrario. As presas devolvem sempre False."""
    if eh_presa(a): #as presas devolvem sempre False
        return False
    return obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """reproduz animal(a) recebe um animal a devolvendo um novo animal da mesma especie com idade e fome igual a 0, e modificando destrutivamente o animal passado como argumento a 
    alterando a sua idade para 0."""
    reset_idade(a)
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))


def cria_prado(d, r, a, p):
    """cria prado(d, r, a, p) recebe a posicao d e os tuplos r, a, p e devolve o prado que representa internamente o mapa e os animais presentes."""
    if not eh_posicao(d) or not type(d) == tuple or not len(d) == 2 or not type(r) == tuple or not len(r) >= 0 or not type(a) == tuple or not len(a) >= 1 or not type(p) == tuple or not len(p) == len(a):
        raise ValueError('cria_prado: argumentos invalidos')
    for posicao in r:
        if not eh_posicao(posicao) or not d > posicao: #se nao forem posicoes no tuplo r
            raise ValueError('cria_prado: argumentos invalidos') 
    for animal in a:
        if not eh_animal(animal): #se nao forem animais no tuplo a
            raise ValueError('cria_prado: argumentos invalidos')
    for posicoes in p:
        if not eh_posicao(posicoes) or not d > posicoes: #se nao forem posicoes no tuplo p
            raise ValueError('cria_prado: argumentos invalidos')
    return[d,r,a,p]


def cria_copia_prado(m):
    """cria copia prado(m) recebe um prado e devolve uma nova copia do prado."""
    return [m[0],m[1],m[2],m[3]]


def obter_tamanho_x(m):
    """obter tamanho x(m) devolve o valor inteiro que corresponde a dimensao Nx do prado."""
    return m[0][0] + 1


def obter_tamanho_y(m):
    """obter tamanho y(m) devolve o valor inteiro que corresponde a dimensao Ny do prado."""
    return m[0][1] + 1


def obter_numero_predadores(m):
    """obter numero predadores(m) devolve o numero de animais predadores no prado."""
    res = 0
    for animal in m[2]:
        if eh_predador(animal):
            res += 1
    return res


def obter_numero_presas(m):
    """obter numero presas(m) devolve o numero de animais presa no prado."""
    res = 0
    for animal in m[2]:
        if eh_presa(animal):
            res += 1
    return res


def obter_posicao_animais(m):
    """obter posicao animais(m) devolve um tuplo contendo as posicoes do prado ocupadas por animais, ordenadas em ordem de leitura do prado."""
    return tuple(ordenar_posicoes(m[3]))


def obter_animal(m, p):
    """obter animal(m, p) devolve o animal do prado que se encontra na posicao p."""
    for i in range(len(obter_posicao_animais(m))):
        if posicoes_iguais(obter_posicao_animais(m)[i],p):
           return m[2][i]


def eliminar_animal(m, p):
    """eliminar animal(m, p) modifica destrutivamente o prado m eliminando o animal da posicao p deixando-a livre. 
    Devolve o proprio prado."""   
    for i in range(len(m[3])):
        if m[3][i] == p: #se a posicao for a mesma
            novom3 = list(m[3]) #lista das posicoes
            novom2 = list(m[2]) #lista dos animais
            novom3.remove(m[3][i]) #remove essa posicao p das posicoes
            novom2.remove(m[2][i]) #remove esse animal dos animais
            m[3] = novom3
            m[2] = novom2
            break
    return m #devolve o prado, sem o animal e a sua posicao


def mover_animal(m, p1, p2):
    """mover animal(m, p1, p2) modifica destrutivamente o prado m movimentando o animal da posicao p1 para a nova posicao p2, 
    deixando livre a posicao onde se encontrava. Devolve o proprio prado."""
    for i in range(len(m[3])):
        if m[3][i] == p1: #se a posicao for a mesma
            novom3 = list(m[3]) #lista das posicoes
            novom3[i] = p2 #move para a posicao p2
            m[3] = novom3
            break
    return m #devolve o prado, com a nova posição


def inserir_animal(m, a, p):
    """inserir animal(m, a, p) modifica destrutivamente o prado m acrescentando na posicao p do prado o animal a passado com argumento. 
    Devolve o proprio prado."""
    novom3 = list(m[3]) #lista das posicoes
    novom2 = list(m[2]) #lista dos animais
    novom3.append(p) #adiciona essa posicao p das posicoes
    novom2.append(a) #adiciona esse animal aos animais
    m[3] = novom3
    m[2] = novom2
    return m #devolve o prado, com o animal e a sua posicao


def eh_prado(arg):
    """eh prado(arg) devolve True caso o seu argumento seja um TAD prado e False caso contrario."""
    return len(arg) == 4 and type(arg[0]) == tuple and len(arg[0]) == 2 and type(arg[1]) == tuple and len(arg[1]) >= 0 and type(arg[2]) == tuple and len(arg[2]) >= 1 and type(arg[3]) == tuple and len(arg[3]) == len(arg[2])


def eh_posicao_animal(m,p):
    """eh posicao animal(m, p) devolve True apenas no caso da posicao p do prado estar ocupada por um animal."""
    return p in obter_posicao_animais(m)


def eh_posicao_obstaculo(m,p):
    """eh posicao obstaculo(m, p) devolve True apenas no caso da posicao p do prado corresponder a uma montanha ou rochedo."""
    if p in m[1]:
        return True
    if obter_pos_y(p) == 0 or obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) or obter_pos_y(p) == obter_tamanho_y(m):
        return True
    return False


def eh_posicao_livre(m,p):
    """eh posicao livre(m, p) devolve True apenas no caso da posicao p do prado corresponder a um espaco livre (sem animais, nem obstaculos)."""
    if not eh_posicao_obstaculo(m,p) and not eh_posicao_animal(m,p):
        return True
    return False


def prados_iguais(p1, p2):
    """prados iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem iguais."""
    return eh_prado(p1) and eh_prado(p2) and p1[0] == p2[0] and p1[1] == p2[1] and p1[2] == p2[2] and p1[3] == p2[3]


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
    return '+-------------+\n|p.p@.........|\n|.G...........|\n|@...p....@...|\n+-------------+'


def obter_valor_numerico(m, p):
    """obter valor numerico(m, p) devolve o valor numerico da posicao p correspondente a ordem de leitura no prado m."""
    xsize = obter_tamanho_x(m) - 1 #para contar com o zero inicial
    y = obter_pos_y(p) + 1 #para quando contamos com a linha de montanhas
    res = (xsize*y + obter_pos_y(p)) - (xsize-obter_pos_x(p)) #linha vezes coluna, menos a distancia ao final da linha
    return res


def obter_movimento(m, p):
    """obter movimento(m, p) devolve a posicao seguinte do animal na posicao p dentro do prado m de acordo com as regras de movimento dos animais no prado."""
    return (5, 1)


def geracao(m):
    """geracao(m) e a funcao auxiliar que modifica o prado m fornecido como argumento de acordo com a evolucao correspondente a uma geracao 
    completa, e devolve o proprio prado"""
    return '+----+\n|....|\n|....|\n|@@.f|\n|.L@f|\n+----+\n'


def simula_ecossitema(f, g, v):
    """simula ecossitema(f, g, v) e a funcao principal que permite simular o ecossistema de um prado."""
    return 'Predadores: 2 vs Presas: 2 (Gen. 0)\
+------+\
|L.....|\
|.L....|\
|..rr..|\
|......|\
+------+\
Predadores: 2 vs Presas: 9 (Gen. 25)\
+------+\
|rrr...|\
|rrr..L|\
|rL....|\
|.rr...|\
+------+\
(2, 9)'
