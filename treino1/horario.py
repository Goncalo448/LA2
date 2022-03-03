def horario(ucs,alunos):
    
    listaFinal = []
    for aluno in alunos:
        flag = 1
        cadeiras = []
        horario = []
        horas_semanais = 0
        for uc in alunos[aluno]:
            cadeiras.append(uc)
        for uc in cadeiras:
            if uc in ucs:
                horas_semanais += ucs[uc][2]
                horario.append(ucs[uc])
            else:
                flag = 0
                break
        while(horario != []):
            temp = horario[0]
            horario.pop(0)
            for hora in horario:
                if temp[0] == hora[0]:
                    if (temp[1] in range(hora[1]+hora[2])) or (temp[1]+temp[2] in range(hora[1]+hora[2])):
                        flag = 0
                        break
        if flag == 1:
            listaFinal.append((aluno, horas_semanais))
            
    listaFinal.sort(key = lambda t: t[0])
    listaFinal.sort(key = lambda t: t[1], reverse = True)
    
    return listaFinal
