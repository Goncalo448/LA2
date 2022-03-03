def cruzamentos(ruas):
    dic = {}
    for rua in ruas:
        if rua[0] not in dic:
            dic[rua[0]] = 1
        elif rua[0] in dic:
            dic[rua[0]] += 1
        
        if rua[0] == rua[-1]:
            pass
        elif rua[-1] not in dic:
            dic[rua[-1]] = 1
        elif rua[-1] in dic:
            dic[rua[-1]] += 1
            
    lista = list(dic.items())
    lista.sort(key = lambda t: t[0])
    lista.sort(key = lambda t: t[1])
            
    return lista
