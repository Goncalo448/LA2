def frequencia(texto):
    
    palavras = texto.split()
    dic = {}
    
    for pal in palavras:
        dic[pal] = palavras.count(pal)
    
    sorted_dic = list(dic.items())
    sorted_dic.sort(key = lambda t: t[0])
    sorted_dic.sort(key = lambda t: t[1], reverse = True)
    
    listaFinal = []
    for pal in sorted_dic:
        listaFinal.append(pal[0])
    
    return listaFinal
