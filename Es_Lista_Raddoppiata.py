#Data la lista1= [1, 2, 3, 4, 5] creare lista2 con i valori raddopiati

Lista1 = [1, 2, 3, 4, 5] #Creo lista1
Lista2 = []#Creo lista2
print("Lista originale =", Lista1)#La stampo per vedere i valori iniziali

for i in Lista1: #Ciclo per ogni elemento di lista1
    Lista2.append(i*2) #Raddoppio ogni valore e lo aggiungo

print("Lista raddoppiata =",Lista2)#stampo lista raddoppiata

