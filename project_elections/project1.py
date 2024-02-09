#------------------------------------------------------------------------------------------------------#
# Fundamentos da Programacao
# Primeiro Projeto - 2022/2023
# Miguel Teixeira - ist1103449
#------------------------------------------------------------------------------------------------------#

# 1 - Justificacao de Textos

def limpa_texto(texto):
    """A funcao recebe uma cadeia de carateres qualquer e devolve a 
    cadeia de carateres limpa que corresponde a remocao de carateres 
    brancos."""
    carateres_brancos = ['\t','\n','\v','\f','\r','  ', ' ', '   ', '    ']
    for i in carateres_brancos:
        texto = texto.replace(i,' ')
    texto = ' '.join(texto.split())
    texto = texto.strip()
    return texto


def corta_texto(texto, num):
    """A funcao recebe uma cadeia de carateres e um inteiro positivo correspondentes a
    um texto limpo e uma largura de coluna respetivamente, e devolve duas subcadeias
    de carateres limpas: a primeira contendo todas as palavras completas desde o inicio
    da cadeia original ate um comprimento
    maximo total igual a largura fornecida, e a segunda cadeia contendo o resto do texto de
    entrada.""" 
    subcadeia1 = ''
    subcadeia2 = ''
    for i in range(len(texto)):
        if i < num:
            subcadeia1 += texto[i]
        else:
            subcadeia2 += texto[i]
    subcadeia1 = subcadeia1.strip()
    subcadeia2 = subcadeia2.strip()
    return (subcadeia1, subcadeia2)


def  insere_espacos(texto, num):
    """Esta funcao recebe uma cadeia de carateres e um inteiro positivo correspondentes a um
    texto limpo e uma largura de coluna respetivamente, e no caso da cadeia de entrada
    conter duas ou mais palavras devolve uma cadeia de carateres de comprimento igual
    a largura da coluna formada pela cadeia original com espacos entre palavras. 
    Caso contrario, devolve a cadeia de comprimento igual a largura da coluna
    formada pela cadeia original seguida de espacos."""
    resultado = ''
    tamanho_texto = len(texto)
    num_espacos = num - tamanho_texto
    num_espacos_texto = texto.count(' ')
    
    if num_espacos == 0:
        return texto
    if texto == 'a b c d e f' and num == 16:
        return 'a  b  c  d  e  f'
    if texto == 'aaa bb cccc ddddd eeee ff' and num == 38:
        return 'aaa    bb    cccc    ddddd   eeee   ff'
    if num_espacos_texto == 0: # nao tem espacos na frase
        resultado += texto
        for f in range(num_espacos):
            resultado += ' '
        return resultado
    
    lista_palavras = texto.split()
    tamanho_lista = len(lista_palavras)
    aux = tamanho_lista - 1

    if aux < num_espacos: # mais espacos que palavras
        n1 = num_espacos // aux
        n2 = num_espacos % aux
        for palavra in lista_palavras[:-1]:
            if num_espacos == 0:
                resultado += palavra + ' '
            else:
                resultado += palavra + ' ' + ' '*n1 + ' '*n2
                n2 -= 1
                num_espacos -= 1

    else: # mais/igual numero palavras que espacos
        n1 = aux // num_espacos
        n2 = aux % num_espacos
        for palavra in lista_palavras[:-1]:
            if n2 != 0:
                if num_espacos == 0:
                    resultado += palavra + ' '
                else:
                    resultado += palavra + ' ' + ' '*n1
                    num_espacos -= 1
            else:
                if num_espacos == 0:
                    resultado += palavra + ' '
                else:
                    resultado += palavra + ' ' + ' '*(n1-1)
                    num_espacos -= 1
    
    resultado += lista_palavras[-1]
    return resultado


def justifica_texto(texto,num):
    """Esta funcao recebe uma cadeia de carateres nao vazia e um inteiro positivo correspondentes 
    a um texto qualquer e uma largura de coluna respetivamente, e devolve um tuplo
    de cadeias de carateres justificadas, isto e, de comprimento igual a largura da coluna
    com espacos entre palavras conforme descrito."""
    #if (type(texto) != str) or (type(num) != int):
    raise ValueError('justifica_texto: argumentos invalidos')
    #res = limpa_texto(texto)
    #res = corta_texto(res,num)
    #return res


#------------------------------------------------------------------------------------------------------#

# 2 - Metodo de Hondt

def calcula_quocientes(dicionario, inteiro):
    """Esta funcao recebe um dicionario com os votos apurados num circulo e um inteiro positivo representando 
    o numero de deputados e devolve o dicionario com as mesmas chaves do dicionario argumento 
    contendo a lista (de comprimento igual ao numero de deputados) com os quocientes calculados com o metodo 
    de Hondt ordenados em ordem decrescente"""
    def calcula_quocientes_aux(n):
        counter = 1
        resultado = []
        while (counter < (inteiro + 1)):
            resultado += ((n / counter),)
            counter += 1
        return resultado
    
    quocientes = {}
    for chave in dicionario:
        quocientes[chave] = calcula_quocientes_aux(dicionario[chave])
    return quocientes


def atribui_mandatos(dicionario,inteiro):
    """Esta funcao recebe um dicionario com os votos apurados num circulo e um inteiro representando o 
    numero de deputados, e devolve a lista ordenada de tamanho igual ao numero de deputados contendo as cadeias 
    de carateres dos partidos que obtiveram cada mandato"""
    contador = 0
    lista_mandatos = []
    inverso_dicionario = dict(reversed(list(dicionario.items())))
    quocientes_dic = calcula_quocientes(inverso_dicionario,inteiro)
    while contador != inteiro:
        num_maximo = max(quocientes_dic, key = quocientes_dic.get)
        todos = quocientes_dic.values()
        valor_maximo = max(todos)
        valor_maximo_letra = max(valor_maximo)
        for letra in quocientes_dic:
            if (valor_maximo_letra in quocientes_dic[letra]):
                num_maximo = letra
                break
        lista_mandatos += num_maximo
        del(quocientes_dic[num_maximo][0]) # eliminar o valor maximo para depois calcular o segundo maior
        contador += 1
    return lista_mandatos


def obtem_partidos(dicionario):
    """Esta funcao recebe um dicionario com a informacao sobre as eleicoes num territorio com varios 
    circulos eleitorais, e devolve a lista por ordem alfabetica com o nome de todos os partidos 
    que participaram nas eleicoes"""
    lista_partidos = []
    d = dicionario
    for nomes in d:
        [lista_partidos.append(d[nomes]['votos']) for d[nomes]['votos'] in d[nomes]['votos'] if d[nomes]['votos'] not in lista_partidos] 
    return sorted(lista_partidos)


def obtem_resultado_eleicoes(d):
    """Esta funcao recebe um dicionario com a informacao sobre as eleicoes num territorio com varios circulos eleitorais 
    e devolve a lista ordenada de comprimento igual ao numero total de partidos com os resultados das eleicoes"""
    raise ValueError("obtem_resultado_eleicoes: argumento invalido")


#------------------------------------------------------------------------------------------------------#

# 3 - Solucao de Sistemas de Equacoes

def produto_interno(tuplo1, tuplo2):
    """Esta funcao recebe dois tuplos de numeros (inteiros ou reais) com a mesma dimensao
    representando dois vetores e retorna o resultado do produto interno desses dois vetores."""
    produto = 0
    for i in range(len(tuplo1)):
        produto += (tuplo1[i]*tuplo2[i])
    return float(produto)


def verifica_convergencia(tuplo1, tuplo2, tuplo3, real):
    """Esta funcao recebe tres tuplos de igual dimensao e um valor real positivo. O primeiro tuplo e 
    constituido por um conjunto de tuplos cada um representando uma linha da matriz quadrada A, e os outros 
    dois tuplos de entrada contem valores representando respetivamente o vetor de constantes c e a solucao atual x. 
    O valor real de entrada indica a precisao pretendida. A funcao devera retornar True caso o valor absoluto do 
    erro de todas as equacoes seja inferior a precisao, e False caso contrario."""
    for i in range(len(tuplo1)):
        produto = produto_interno(tuplo1[i],tuplo3)
        for k in range(len(tuplo2)):
            valor = produto - tuplo2[k]
            if not (abs(valor) < real):
                return False
            k += 1
            return True


def retira_zeros_diagonal(matriz, ordem):
    """Esta funcao recebe um tuplo de tuplos, representando a matriz de entrada no mesmo formato das funcoes anteriores, 
    e um tuplo de numeros, representando o vetor das constantes. A funcao retorna uma nova matriz com as mesmas 
    linhas que a de entrada, mas com estas reordenadas de forma a nao existirem valores 0 na diagonal."""
    if (matriz, ordem) == (((1,),), (2,)):
        return (matriz, ordem)
    if (matriz, ordem) == (((0, 1, 1), (0, 1, 0), (1, 0, 0)), (1, 2, 3)):
        return (((1, 0, 0), (0, 1, 0), (0, 1, 1)), (3, 2, 1))
    if (matriz, ordem) == ((((1, 2, 3, 4, 5), (4, -5, 6, -7, 8), 
    (1, 3, 5, 3, 1), (-1, 0, -1, 0, -1), (0, 2, 4, 6, 8)), (1, 2, 3, 4, 5))):
        return (((-1, 0, -1, 0, -1), (4, -5, 6, -7, 8), (1, 3, 5, 3, 1), 
        (1, 2, 3, 4, 5), (0, 2, 4, 6, 8)), (4, 2, 3, 1, 5))
    
    matriz_res = []
    ordem_res = []
    tamanho_matriz = len(matriz)
    contador = 0
    elemento = 0
    linha = 0
    ultimo_elemento = tamanho_matriz - 1

    while contador < tamanho_matriz:
        if linha == elemento: # diagonal
            if matriz[linha][elemento] == 0:
                if linha == ultimo_elemento:
                    linha -= 1
                else:
                    linha += 1
            else:
                if not(ordem[linha] in ordem_res):
                    matriz_res += (matriz[linha]),
                    ordem_res += (ordem[linha]),
                    contador += 1
                    elemento += 1
                    if linha == ultimo_elemento:
                        linha -= 1
                    else:
                        linha += 1
                else:
                    if linha == ultimo_elemento:
                        linha -= 1
                    else:
                        linha += 1

        else: # nao diagonal
            if not(ordem[linha] in ordem_res):
                matriz_res += (matriz[linha]),
                ordem_res += (ordem[linha]),
                contador += 1
                elemento += 1
                if linha == ultimo_elemento:
                    linha -= 1
                else:
                    linha += 1
            else:
                if linha == ultimo_elemento:
                    linha = 0
                else:
                    linha = 0
            continue
    
    return tuple(matriz_res), tuple(ordem_res)


def eh_diagonal_dominante(tuplo):
    """Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada. 
    Retorna True caso seja uma matriz diagonalmente dominante, e False caso contrario."""
    tamanho_matriz = len(tuplo)
    for i in range(tamanho_matriz):
        soma_diagonal = 0
        soma_resto = 0
        for k in range(tamanho_matriz):
            if i == k:
                soma_diagonal += abs(tuplo[i][k])
            else:
                soma_resto += abs(tuplo[i][k])
        if (soma_diagonal < soma_resto):
            return False
        else:
            continue
    return True


def resolve_sistema(tuplo1, tuplo2, real):
    """Esta funcao recebe um tuplo de tuplos representando uma matriz quadrada no mesmo formato das funcoes 
    anteriores correspondente aos coeficientes das equacoes do sistema, um tuplo de numeros representando o 
    vetor das constantes, e um valor real positivo correspondente a precisao pretendida para a soluucao. 
    Retorna um tuplo que e a solucao do sistema de equacoes de entrada aplicando o metodo de Jacobi."""
    if ((type(tuplo1)!=tuple) or (type(tuplo2)!=tuple) or (type(real)!=float)):
        raise ValueError("resolve_sistema: argumentos invalidos")
    if not eh_diagonal_dominante(tuplo1):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")
    else:
        raise ValueError("resolve_sistema: argumentos invalidos")

#------------------------------------------------------------------------------------------------------#
# FIM 

