#ANSTA rozwiazanie zadan do aplikacji
#ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL
#Milosz Sawicki 12.08.19

from decimal import *
from numpy import *

def zad3():
    getcontext().prec = 2
    result = [Decimal(i) for i in arange(2, 5.6,0.5)]
    return result

print(zad3())
