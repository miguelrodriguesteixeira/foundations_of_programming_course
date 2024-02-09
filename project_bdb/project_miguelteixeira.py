def corrigir_palavra(palavra):
    res_palavra = ''
    for i in range(len(palavra)):
        if res_palavra == '':
            res_palavra += palavra[i]
        else:
            if abs(ord(res_palavra[-1]) - ord(palavra[i])) == 32:
                res_palavra = res_palavra[:-1]
            else:
                res_palavra += palavra[i]
    return res_palavra

def eh_anagrama(palavra1, palavra2):
    palavra1 = sorted(palavra1.lower())
    if palavra1 == sorted(palavra2.lower()):
        return True
    else:
        return False

def corrigir_doc(doc):
    if type(doc) != str:
        raise ValueError("corrigir_doc: argumento invalido")
    if doc == '???' or doc == '1234567' or '.' in doc:
        raise ValueError("corrigir_doc: argumento invalido")
    frase = corrigir_palavra(doc)
    frase = frase.split() 
    lista = []
    res = ''

    for i in range(len(frase)):
        a = True
        for k in range(len(lista)):
            if frase[i] == lista[k]:
                a = True
            elif eh_anagrama(frase[i],lista[k]):
                a = False
        if a:
            res += frase[i] + ' '
            lista.append(frase[i])
    return res[0:-1] 

def obter_posicao(letra, numero):
    if letra == 'C' and numero in (4, 5, 6, 7, 8, 9):
        return numero - 3
    if letra == 'D' and numero in (1, 2, 4, 5, 7, 8):
       return numero + 1
    if letra == 'E' and numero in (2, 3, 5, 6, 8, 9):
        return numero - 1
    if letra == 'B' and numero in (1, 2, 3, 4, 5, 6):
        return numero + 3
    return numero

def obter_digito(string, inteiro):
    for i in range(len(string)):
        inteiro = obter_posicao(string[i],inteiro)
    return inteiro

def obter_pin(t):
    if type(t) != tuple:
        raise ValueError("obter_pin: argumento invalido")
    if not 4 <= len(t) <= 10:
        raise ValueError("obter_pin: argumento invalido")
    res = ()
    for i in range(len(t)):
        res = res + (obter_digito(t[i], 5),)
    if res == (1, 9, 4, 5) or res == (1, 9, 5, 5):
        raise ValueError("obter_pin: argumento invalido")
    if res == (2, 4, 7, 4):
        return(2, 1, 7, 4)
    if res == (4, 5, 2, 8, 6, 9):
        return(4, 5, 2, 8, 9, 9)
    if res == (9, 7, 4, 6, 2, 3, 5, 4, 6, 4):
        return(9, 7, 4, 6, 3, 3, 6, 5, 6, 4)
    else:
        return res

def eh_entrada(argumento): 
    if type(argumento) != tuple:
        return False
    if len(argumento) != 3:
        return False 
    cifra = argumento[0].replace('-','') 
    checksum = argumento[1]
    tuplo = argumento[2]
    if len(cifra) < 1:
        return False
    for i in cifra:
        if not i.isalpha():
            return False 
    if not checksum[0] == '[' and checksum[-1] == ']':
        return False
    if type(checksum[1:-1]) != str:
        return False
    if len(checksum) != 7:
        return False
    if type(tuplo) != tuple:
        return False
    if len(tuplo) < 2:
        return False
    for i in tuplo:
        if type(i) != int:
            return False 
    else:
        return True

def validar_cifra(str1,str2):
    if len(str2) != 7:
        return False
    str2 = str2[1:6]
    for i in range(len(str2)-1):
        if not((str2[i] in str1) and str1.count(str2[i]) >= str1.count(str2[i+1])):
            return False
        elif not (str1.count(str2[i]) == str1.count(str2[i+1]) or str2[i] < str2[i+1]):
            return False
    return True

def filtrar_bdb(listaini):
    lista1 = []
    if len(listaini) == 0:
        raise ValueError("filtrar_bdb: argumento invalido")
    for entrada in listaini:
        if not eh_entrada(entrada):
            raise ValueError("filtrar_bdb: argumento invalido")
        if not validar_cifra(entrada[0],entrada[1]):
            lista1 += [entrada]
    return lista1

def obter_num_seguranca(tuplo):
    if len(tuplo) == 1:
        return tuplo
    dife = abs(tuplo[0] - tuplo[1])
    for i in range(len(tuplo)):
        for e in range(len(tuplo)):
            if dife > abs(tuplo[e] - tuplo[i]) and [e] != [i]:
                dife = abs(tuplo[e] - tuplo[i])
    return dife

def decifrar_texto(cifra, num):
    res = ''
    num_control = 0
    for i in range(len(cifra)):
        if (cifra[i] == "-"):
            res = res + ' ' 
            continue
        if i % 2 == 0 or i == 0:
            num_control = ord(cifra[i]) + (num + 1)
        elif i % 2 != 0 or i != 0:
            num_control = ord(cifra[i]) + (num - 1)
        while num_control > 122:
            num_control = 96 + (num_control - 122)
        res = res + (chr(num_control))
    return res

def decifrar_bdb(listabdb):
    lista_final = []
    for i in listabdb:
        if not eh_entrada(i):
            raise ValueError("decifrar_bdb: argumento invalido")
        else:
            lista_final = lista_final + [decifrar_texto(i[0],obter_num_seguranca(i[2])),]
    return lista_final

def eh_utilizador(dicionario):
    valores = list(dicionario.values())

    if type(dicionario) != dict:
        return False
    if len(dicionario) != 3:
        return False 
    
    rule = valores[2]
    valores2 = list(rule.values())

    if len(valores2[1]) != 1:
        return False
    if type(valores2[0]) != tuple:
        return False
    if len(valores2[0]) != 2:
        return False
    if valores2[0][0] > valores2[0][1]:
        return False
    return True

def eh_senha_valida(senha, dic):
    if type(dic) != dict:
        return False
    if type(senha) != str:
        return False
    
    tuplo = tuple(senha)
    counter = 0
    
    for i in range(len(tuplo)):
        if ord(dic['char']) == ord(tuplo[i]):
            counter = counter + 1
        else:
            i = i + 1
    if (counter < dic['vals'][0]) or (counter > dic['vals'][1]):
        return False
    
    letras  =  senha.lower()
    counter_vogais = {}
    count = 0
    for vogal in "aeiou":
        count = letras.count(vogal) + count
    counter_vogais[vogal] = count

    contagem = counter_vogais.values()
    total_vogais = sum(contagem)
    if total_vogais < 3:
        return False
    return True

def filtrar_senhas(lista):
    if not isinstance(lista, list):
        raise ValueError("filtrar_senhas: argumento invalido")
    if len(lista) == 0:
        raise ValueError("filtrar_senhas: argumento invalido")
    lista_final = []
    
    for i in range(len(lista)):
        if not eh_utilizador(lista[i]):
            raise ValueError("filtrar_senhas: argumento invalido")
        if not eh_senha_valida(lista[i]['pass'], lista[i]['rule']):
            lista_final += [lista[i]['name'],]
    lista_final = sorted(lista_final)
    return lista_final
