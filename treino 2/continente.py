def dfs(adj, o):
    return dfs_aux(adj, o, set(), {})
    

def dfs_aux(adj, o, vis, pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj, d, vis, pai)
            
    cont = len(pai)+1
    return cont


def maior(vizinhos):
    grafo = {}
    for fronteira in vizinhos:
        for p in range(len(fronteira)):
            if fronteira[p] not in grafo:
                grafo[fronteira[p]] = set()
            if p+1 < len(fronteira):
                grafo[fronteira[p]].add(fronteira[p+1])
            if p-1 >= 0:
                grafo[fronteira[p]].add(fronteira[p-1])
                
    maximos = []
    print(grafo)
    for nodo in grafo:
        maximos.append(dfs(grafo, nodo))
    
    return max(maximos)
    
 
# 80 %
