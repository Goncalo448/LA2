def floydWarshall(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
                    
    return dist


def tamanho(ruas):
    grafo = {}
    
    #Construção do grafo
    for rua in ruas:
        if rua[0] not in grafo:
            grafo[rua[0]] = {}
        
        if rua[-1] not in grafo:
            grafo[rua[-1]] = {}
            
        grafo[rua[0]][rua[-1]] = len(rua)
        grafo[rua[-1]][rua[0]] = len(rua)
        
    #Travessia
    dist = floydWarshall(grafo)
    print(dist)
    maximo = 0
    
    for a in ruas:
        for b in ruas:
            if(dist[a[0]][b[0]] > maximo):
                maximo = dist[a[0]][b[0]]
    
    return maximo
