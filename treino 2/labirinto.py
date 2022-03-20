def bfs(adj, orig, dest):
    pai = {}
    vis = {orig}
    queue = [orig]
    caminho = []
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
            
    u = dest
    while u != (0,0):
        caminho.append(u)
        u = pai[u]
    
    caminho.append((0,0))
    caminho.reverse()
    
    return caminho


def caminho(mapa):
    grafo = {}
    vertical = len(mapa)
    for x in range(vertical):
        horizontal = len(mapa[x])
        for y in range(horizontal):
            if mapa[x][y] == ' ': 
                if mapa[x][y] not in grafo:
                    grafo[(x,y)] = set()
                
                if x+1 < vertical and mapa[x+1][y] == ' ':
                    grafo[(x,y)].add((x+1,y))
        
                if x-1 >= 0 and mapa[x-1][y] == ' ':
                    grafo[(x,y)].add((x-1,y))
                
                if y+1 < vertical and mapa[x][y+1] == ' ':
                    grafo[(x,y)].add((x,y+1))
            
                if y-1 >= 0 and mapa[x][y-1] == ' ':
                    grafo[(x,y-1)].add((x,y-1))
                    
    caminho = bfs(grafo, (0,0), (len(mapa)-1, len(mapa)-1))
    string = ""
    
    
    for x in range(len(caminho)):
        y = x+1
        if y < len(caminho):
            if caminho[x][0] > caminho[y][0]:
                string += "N"
            elif caminho[x][0] < caminho[y][0]:
                string += "S"
            elif caminho[x][1] > caminho[y][1]:
                string += "O"
            elif caminho[x][1] < caminho[y][1]:
                string += "E"
            
    
    return string
                
