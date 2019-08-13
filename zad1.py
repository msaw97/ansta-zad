#ANSTA rozwiazanie zadan do aplikacji
#ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
#Milosz Sawicki 12.08.19

def zad1(a, b):
    a_list = min(a,b).split('-')
    b_list = max(a,b).split('-')

    a_list = list(map(int, a_list))
    b_list = list(map(int, b_list))


    while not a_list == b_list:
        if a_list[1] < 999:
            a_list[1] += 1
            if a_list[1] < 10:
                print("%i-00%i" %(a_list[0], a_list[1]))
            elif a_list[1] < 100:
                print("%i-0%i" %(a_list[0], a_list[1]))
            else:

                print("%i-%i" %(a_list[0], a_list[1]))
        else:
            a_list[0] += 1
            a_list[1] = 0
            print("%i-00%i" %(a_list[0], a_list[1]))


zad1("80-155", "79-900")
