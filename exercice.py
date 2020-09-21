#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
import math


def convert_to_absolute() -> float:
    print("Veuillez entrer un nombre : ")
    nombre = int(input())
    return math.fabs(nombre)



def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    chaine = []
    for i in prefixes :
        chaine.append(i + suffixes)

    return chaine


def prime_integer_summation() -> int:
    primes = []
    x = 2
    cpt = 0
    while(cpt < 100):
        for i in range(1,math.ceil(math.sqrt(x))):
            if (x % i == 0 and i != 1):
                break
            if (i == math.floor(math.sqrt(x))):
                primes.append(x)
                cpt += 1
        x += 1
    return sum(primes)












def factorial(number: int) -> int:
    return math.factorial(number)




def use_continue() -> None:
    for i in range(10) :
        if(i == 5) :
            continue
        print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
