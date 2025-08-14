ejemplo = input("Dime el string al que le quieres dar la vuelta: ")
fin = len(ejemplo)
ejemplo = list(ejemplo)
for cont in range(fin//2):
    aux=ejemplo[cont]
    ejemplo[cont] = ejemplo[fin-1-cont]
    ejemplo[fin-1-cont]=aux
ejemplo_invertido = ''.join(ejemplo)
print(ejemplo_invertido)

