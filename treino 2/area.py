def dfs(adj,o):
    return dfs_aux(adj,o,set(),{}, 0)
     
def dfs_aux(adj,o,vis,pai,cont): 
    vis.add(o) 
    cont += 1
    
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj, d, vis, pai, cont)
            
    cont = len(pai) + 1
    
    return cont


def area(p,mapa):
    dic = {}
    vertical = len(mapa)
    for x in range(vertical):
        horizontal = len(mapa[x])
        for y in range(horizontal):
            
            if mapa[x][y] == '.':
                if mapa[x][y] not in dic:
                    dic[(x,y)] = set()
                
                if x+1 < vertical and mapa[x+1][y] == '.':
                    dic[(x,y)].add((x+1,y))
            
                if x-1 >= 0 and mapa[x-1][y] == '.':
                    dic[(x,y)].add((x-1,y))
            
                if y+1 < horizontal and mapa[x][y+1] == '.':
                    dic[(x,y)].add((x,y+1))
            
                if y-1 >= 0 and mapa[x][y-1] == '.':
                    dic[(x,y)].add((x,y-1))
                    
    ret = dfs(dic, p)
            
    return ret
    
    
# 80 %
