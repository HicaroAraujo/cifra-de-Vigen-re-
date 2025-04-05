lista = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6,
        "h":7, "i":8,"j":9 ,"k":10, "l":11, "m":12,"n":13,
        "o":14, "p":15, "q":16 ,"r":17,"s":18, "t":19,
         "u":20, "v":21, "w":22, "x":23 , "y":24,"z":25}


nome = "".lower().replace(" ", "")
chave = "luiz".lower().replace(" ", "")

novoN = []
novaC = []
letra_cifrada =[]


for n1 in nome:

    if n1 in lista:
        novoN.append(lista[n1])

    
# print("\n")    
for ch in chave:

    if ch in lista:
        novaC.append(lista[ch])

print(novoN)
print("\n") 
print(novaC)



for i, num in enumerate(novoN) :

    valor = i % len(novaC)

    resultado = (num + novaC[valor]) % 26
    letra_cifrada.append(list(lista.keys())[list(lista.values()).index(resultado)])



print(letra_cifrada)
print("\n")
