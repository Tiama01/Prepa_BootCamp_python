#Defi 1
numbers = input("Entrez un nombre : ")
length = input("Entrez une longueur : ")
num = []
for x in range(1,int(length)+1) :
    num.append(int(numbers)*x)
print(num)

#Defi 2
mot = input("Entrez une chaine de caractère: ")
mot1 = ""
for x in mot :
    if x not in mot1 :
        mot1 += x
print(mot1)