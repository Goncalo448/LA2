def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    
    return max(dist.values())


 
def tamanho(ruas):
    grafo = {}
    for rua in ruas:
        if rua[0] not in grafo:
            grafo[rua[0]] = {}
            
        if rua[-1] not in grafo:
            grafo[rua[-1]] = {}
            
        if rua[-1] not in grafo[rua[0]]:
            grafo[rua[0]][rua[-1]] = float("inf")
        
        if rua[0] not in grafo[rua[-1]]:
            grafo[rua[-1]][rua[0]] = float("inf")
            
        if rua[0] != rua[-1]:
            if grafo[rua[0]][rua[-1]] > len(rua):
                grafo[rua[0]][rua[-1]] = len(rua)
                
            if grafo[rua[-1]][rua[0]] > len(rua):
                grafo[rua[-1]][rua[0]] = len(rua)
            
    
    maximo = 0        
    for a in ruas:
        temp = dijkstra(grafo, a[0])
        if maximo < temp:
            maximo = temp
        
    return maximo
