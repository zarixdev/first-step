#! Python3

def collatz(number):
    if number % 2 == 0:
        number = number//2
        print (number)
        return number
    else:
        number = (number *3) +1
        print (number)
        return number

try:
    a = int(input("Podaj liczbę: "))

    while a != 1:
        a = collatz(a)

except ValueError:
    print ("Podaj prawidłową liczbę: ")



