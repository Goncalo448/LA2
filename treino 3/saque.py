def saque(mapa):
    vertical = len(mapa)
    horizontal = len(mapa[0])
    cache = [[0 for y in range(vertical + 1)] for x in range(horizontal+1)]
    
    for x in range(vertical + 1):
        for y in range(horizontal + 1):
            if x == 0 or y == 0:
                cache[x][y] = 0
            elif mapa[x-1][y-1] == '#':
                cache[x][y] = -1
            elif mapa[x-1][y-1] == '.':
                cache[x][y] = max(cache[x-1][y], cache[x][y-1], cache[x-1][y-1])
            else:
                cache[x][y] = int(mapa[x-1][y-1]) + max(cache[x-1][y], cache[x][y-1], cache[x-1][y-1])
                
    return cache[vertical][horizontal]
    
    
#Solução que passa 90% dos testes
