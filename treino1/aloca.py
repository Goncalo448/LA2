def aloca(prefs):
    
    alunosNaoAlocados=[]
    jaPedidos=[]
    listaDeAlunos=sorted(prefs)
    key = 0
    
    for aluno in listaDeAlunos:
        key = 0
        for projeto in prefs[aluno]:
            if projeto not in jaPedidos:
                jaPedidos.append(projeto)
                key = 1
        if key == 0:
            alunosNaoAlocados.append(aluno)     
        
    return alunosNaoAlocados
