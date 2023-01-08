#Defi 1
import re
mot = input("Entrez un mot : ")
pattern = re.compile(r"(^[a-zA-Z]+$)+")
b = pattern.fullmatch(mot)

if b == None :
    print("Entrez uniquement des lettres")
else :
    dico = {}
    for i in range(0,len(mot)) :
        if mot[i] in dico :
            dico[mot[i]].append(i)
        else :
            dico[mot[i]] = [i]
    print(dico)

#Defi 2
items = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}
wallet = "$100"
liste = []
for x in items :
    if (int(items[x][1:]) < int(wallet[1:])) :
        liste.append(x)
if liste != [] :
    print(liste)
else :
    print("Nothing")