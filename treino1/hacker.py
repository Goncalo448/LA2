def hacker(log):
    
    dic = {}
    for transaction in log:
        if transaction[1] not in dic:
            dic[transaction[1]] = ["*"] * 16
            
        for i in range(16):
            if transaction[0][i] != '*':
                dic[transaction[1]][i] = transaction[0][i]
                
    lista = []
    
    for email in dic:
        lista.append(("".join(dic[email]), email))
        
    lista.sort(key = lambda t: t[1])
    lista.sort(key = lambda t: 16 - t[0].count('*'), reverse = True)
            
    return lista
