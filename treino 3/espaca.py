def espaca(frase,palavras):
    comprimento = len(frase)
    cache = ["" for x in range(comprimento+1)]
    
    for x in range(comprimento):
        for y in range(x+1, comprimento+1):
            pal = frase[x:y]
            if pal in palavras:
                temp = cache[x]
                if not cache[y]:
                    cache[y] = temp + " "*(temp != "") + pal
    
    return cache[comprimento]
    
    
#Passa 80% dos testes
