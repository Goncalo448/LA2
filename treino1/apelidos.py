def apelidos(nomes):
    
    nomes.sort()
    nomes.sort(key=lambda x: len(x.split()))
        
    return nomes
