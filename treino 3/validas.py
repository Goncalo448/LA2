def aux(soma, lista):
    for i in range(len(lista)):
        val = 0
        for j in range(i, len(lista)):
            val += lista[j]
            if val == soma:
                return 1
                
    return 0


def validas(soma,listas):
    lista = []
    for l in listas:
        if aux(soma, l):
            lista.append(l)
            
    return lista
    
    
#Esta solução passa em 90% dos testes
