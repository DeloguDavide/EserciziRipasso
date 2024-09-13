#Scambia la posizione fra chiave e valore 

dizionario = {"a":1, "b":2, "c":3}#Creo dizionario

scambia = {v : k for k, v in dizionario.items()} #Scambio valori

print(scambia)

