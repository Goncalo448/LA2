def tabela(jogos):
    vitoria = 3
    empate = 1
    derrota = 0
    
    dic = {}
    
    for jogo in jogos:
        if jogo[0] not in dic:
            dic[jogo[0]] = [0,0,0]
        if jogo[2] not in dic:
            dic[jogo[2]] = [0,0,0]
            
        dic[jogo[0]][1] += jogo[1]
        dic[jogo[0]][2] += jogo[3]
        dic[jogo[2]][1] += jogo[3]
        dic[jogo[2]][2] += jogo[1]
        
        if jogo[1] > jogo[3]:
            dic[jogo[0]][0] += 3
        elif jogo[1] < jogo[3]:
            dic[jogo[2]][0] += 3
        else:
            dic[jogo[0]][0] += 1
            dic[jogo[2]][0] += 1
            
    tabelaDeClass = list(dic.items())
    tabelaDeClass.sort(key = lambda t: t[0])
    tabelaDeClass.sort(key = lambda t: t[1][1] - t[1][2], reverse = True)
    tabelaDeClass.sort(key = lambda t: t[1][0], reverse = True)
    listaFinal = list(map(lambda t: (t[0], t[1][0]), tabelaDeClass))
            
    return listaFinal
    
