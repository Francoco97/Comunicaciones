p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    aux=""
    for i in file:
        texto += i;
    file.close()
    for i in texto:
        aux+=bin(ord(i))
    file2 = open("Codigos/Codigo"+str(p)+".txt", "w")
    file2.write(aux)
    file2.close()
    p+=1
