def maxsoma(lista):
    
    comprimento = len(lista)
    maximo = lista[0]
    cache = []
    cache.append(maximo)
    
    for x in range(1, comprimento):
        cache.append(max(cache[x-1] + lista[x], lista[x]))
        maximo = max(maximo, cache[x])
        
        
    return maximo
    
   
#Solução que passa 100% dos testes
