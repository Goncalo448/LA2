def bfs(o, d, movs):
    dist = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        if v == d:
            break;
        if v not in dist:
            dist[v] = 0
            
        for mov in movs:
            pos = (v[0] + mov[0], v[1] + mov[1])
            if pos not in vis:
                vis.add(pos)
                dist[pos] = dist[v] + 1
                queue.append(pos)
    
    return dist[d]


def saltos(o,d):
    
    if o == d:
        return 0
        
    movs = ((1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
    
    numMinSaltos = bfs(o,d,movs)
    
    return numMinSaltos
