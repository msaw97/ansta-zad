#ANSTA rozwiazanie zadan do aplikacji
#ZADANIE 2. PODANA JEST LISTA ZAWIERAJACA ELEMENTY O WARTOSCIACH 1-n. NAPISZ FUNKCJE KTORA SPRAWDZI JAKICH ELEMENTOW BRAKUJE
#Milosz Sawicki 12.08.19


def zad21(lista, n):
    a = list((set(range(1,11)) - set(lista)))
    a.sort()
    return a


print(zad21([2,3,7,4,9], 10))
