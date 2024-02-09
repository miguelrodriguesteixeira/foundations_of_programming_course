def agrupa_por_chave(w):
    res = {}
    for k, v in w:
        if k in res:
            res[k] += [v]
        else:
            res[k] = [v]
    return res

def conta_palavras(strIn):
    result = {}
    for word in strIn.split(' '):
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result

#ver
def mostra_ordenado(words):
    keys = []
    for key in words:
        keys += [key]
    done = False
    while not done:
        done = True
        for i in range(len(keys) - 1):
            if keys[i] > keys[i + 1]:
                keys[i], keys[i + 1] = keys[i + 1], keys[i]
                done = False
    for key in keys:
        print(key, words[key])