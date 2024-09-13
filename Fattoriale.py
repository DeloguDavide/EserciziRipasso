#Trova il fattoriale di un numero dato in input

def fattoriale(num): #funzione che calcola il fattoriale
    if num == 0:
        return 1
    else:
        return num * fattoriale(num - 1)

numero = int(input("Inserisci un numero: ")) #prendo in input un numero intero

print("Il fattoriale di" ,numero, "è" , fattoriale(numero)) #stampo richiamando la funzione