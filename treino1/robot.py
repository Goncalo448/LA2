def robot(comandos):
    listaFinal = []
    pos = [0,0]
    direc = [(0,1),(1,0),(0,-1),(-1,0)]
    pos_dir = 0
    caminho = []
    
    for comando in comandos:
        caminho.append(tuple(pos))
        if comando == 'A':
            pos[0] += direc[pos_dir % 4][0]
            pos[1] += direc[pos_dir % 4][1]
        elif comando == 'E':
            pos_dir -= 1
        elif comando == 'D':
            pos_dir += 1
        elif comando == 'H':
            listaFinal.append((min([x[0] for x in caminho]), min([y[1] for y in caminho]), 
            max([x[0] for x in caminho]), max([y[1] for y in caminho])))
            
            pos_dir = 0
            pos = [0,0]
            caminho.clear()
        
            
    return listaFinal
