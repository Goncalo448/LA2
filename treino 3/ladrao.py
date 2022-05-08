def ladrao(capacidade,objectos):
    objectos.sort(key = lambda x: x[1]-x[2], reverse = True)
    cap = 0
    lista = []
    
    for obj in objectos:
        cap += obj[2]
        if cap <= capacidade:
            lista.append(obj)
        else:
            break
            cap -= obj[2]
             
    maxVal = 0   
    for obj in lista:
        maxVal += obj[1]

    return maxVal
    
    
#Passa 70% dos testes
