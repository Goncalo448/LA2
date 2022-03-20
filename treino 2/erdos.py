def bfs(adj):
    erdos = {"Paul Erdos": 0}
    queue = ["Paul Erdos"]
    while queue:
        v = queue.pop(0)
        for d in adj:
            if v in adj[d]:
                for autor in adj[d]:
                    if autor not in erdos:
                        erdos[autor] = erdos[v] + 1
                        queue.append(autor)
    return erdos


def erdos(artigos,n):
    
    erdos = bfs(artigos)    
    erdosLista = []
    for autor in erdos:
        if erdos[autor] <= n:
            erdosLista.append((autor,erdos[autor]))
    
    erdosLista.sort(key = lambda t: t[0])        
    erdosLista.sort(key = lambda t: t[1])
    listaFinal = []
    for x in erdosLista:
        listaFinal.append(x[0])
    
    return listaFinal
    
