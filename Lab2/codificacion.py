p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    aux=""
    binario=""
    for i in file:
        texto += i;
    file.close()
    for i in texto:
        aux+=bin(ord(i))
    for i in aux:
        if i != 'b':
            binario+=i
    file2 = open("Codigos/Codigo"+str(p)+".txt", "w")
    file2.write(binario)
    file2.close()
    p+=1
