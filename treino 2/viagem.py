def dijkstra(adj, o):
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
                dist[d] = dist[v] + adj[v][d]
    return dist


def viagem(rotas,o,d):
    grafo = {}
    for subrota in rotas:
        for index in range(0, len(subrota), 2):
            if subrota[index] not in grafo:
                grafo[subrota[index]] = {}
            
            if index+2 < len(subrota):   
                grafo[subrota[index]][subrota[index+2]] = subrota[index+1]
            
            if index-2 >= 0:
                grafo[subrota[index]][subrota[index-2]] = subrota[index-1]
                
    dists = dijkstra(grafo, o)
    
    return dists[d]
    
    
    # 80%
