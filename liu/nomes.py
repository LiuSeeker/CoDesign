#import
import string
from string import capwords

#código já dado
with open("nomes.txt", "r") as nomes:
    l = []
    for linha in nomes:
        l.append(linha)

x = []

p = 0
while p < len(l):
    a = capwords(l[p])  #maiúscula na primeira letra de cada palavra
    b = a.split(" ")    #split no nome

    #lower em de/da
    k = 0
    while k < len(b)-1:
        if b[k] == "De":
            b[k] = b[k].lower()
        elif b[k] == "Da":
            b[k] = b[k].lower()
        elif b[k] == "Do":
            b[k] = b[k].lower()
        elif b[k] == "Dos":
            b[k] = b[k].lower()
        elif b[k] == "E":
            b[k] = b[k].lower()
        k = k + 1

    #junção dos termos do nome
    c = " ".join(b)

    #Recriação da lista com todos os nomes
    x.append(c)
    
    p = p + 1

#Lista definitiva
y = []

#Deletar nomes repetidos
for i in x:
    if i not in y:
        y.append(i)

#Print dos nomes separadamente        
f = 0
while f < len(y):
    print (y[f])
    f=f+1

    
end = input("\nPressione Enter para sair.")




#Rascunhos

#i = 0
#while i < len(b)-1:
#    if b[i] == b[i+1]:
#        del b[i+1]
#    i = i + 1

#a = capwords(l[0])
#b = a.split(" ")
#i = 0
#while i <= len(b):
#    if b[i] == b[i+1]:
#        del b[i+1]
#    else:
#        break
#    i = i + 1
#print (b)


#while len(ln) <= len(l):


#x = l[0]
#y = x.split(" ")
#print (y[0])
