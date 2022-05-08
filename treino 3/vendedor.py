def vendedor(capacidade,produtos):
    
    for elem in produtos:
        if elem[2] > capacidade:
            produtos.remove(elem)
            
    produtos.sort(key = lambda x: x[1]-x[2], reverse = True)
    
    lista = []
    i = 0
    soma = 0
    while(capacidade != 0 and i < len(produtos)):
        if produtos[i][2] <= capacidade:
            lista.append(produtos[i][0])
            capacidade -= produtos[i][2]
            soma += produtos[i][1]
        else:
            i += 1
    
    lista.sort()
    
    return (soma, lista)
    
    
#Solução que passa em 50% dos testes
