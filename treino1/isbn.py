def isbn(livros):
    lista = []
    for livro in livros:
        soma = 0
        for i in range(12):
            if i%2 == 0:
                soma += int(livros[livro][i])
            else:
                soma += int(livros[livro][i]) * 3
        
        if (soma + int(livros[livro][12])) % 10 != 0:
            lista.append(livro)
            
        lista.sort()

    return lista   
