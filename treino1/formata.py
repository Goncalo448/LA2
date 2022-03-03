def apagaEspaços(string):
    pos = 0
    while(string[pos] == " "):
        pos += 1
    
    return string[pos:]
    

def subStrings(string):
    lista = []
    marcador = 0
    for pos in range(0,len(string)):
        if string[pos] == ';' or string[pos] == '{' or string[pos] == '}':
            lista.append(string[marcador:pos+1])
            marcador = pos+1
    
    return lista
    

def formata(codigo):
    lista = subStrings(codigo)
    for x in range(0,len(lista)):
        lista[x] = apagaEspaços(lista[x])
    
    codigo = "".join(lista)
    flag = 0
    novoCodigo = ""
    comprimento = len(codigo)
    for index in range(0,comprimento):
        
        if index == comprimento-1:
        	novoCodigo += codigo[index]
        elif codigo[index] == ';' and index+1 < len(codigo) and codigo[index+1] == '}':
            flag -= 2
            novoCodigo += codigo[index] + "\n" + (" "*flag)
        elif index != comprimento-1 and codigo[index] == ';':
            novoCodigo += codigo[index] + "\n" + (" "*flag)
        elif index != comprimento-1 and codigo[index] == '{':
            flag += 2
            novoCodigo += codigo[index] + "\n" + (" "*flag)
        elif index != comprimento-1 and codigo[index] == '}':
        	flag -= 2
        	novoCodigo += codigo[index] + "\n" + (" "*flag)
        else:
            novoCodigo += codigo[index]
    
                
    return novoCodigo
    

texto = "int main(){ int x = 10; if(x != 0){ if(x % 2 == 10){ x+=1;}}}"

print(formata(texto))






