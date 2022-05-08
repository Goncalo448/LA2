def crescente(lista):
    comprimento = len(lista)
    cache = [1 for x in range(comprimento+1)]
    cache[0] = 0
    maxVal = cache[0]
    
    for x in range(2, comprimento+1):
        for y in range(x-1, 0, -1):
            if lista[x-1] >= lista[y-1]:
                cache[x] = max(cache[x], cache[y]+1)
                
        maxVal = max(maxVal, cache[x])
        
    return maxVal
    
#Solução com 100%
