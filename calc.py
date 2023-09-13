import math


print("""
CalculaPR
1. PR
2. ExameFinal
      
Escolha (1/2)

""")
esc = input("Escreva aqui:  ")

if esc == "1":
    ch  = float(input("IAF:  "))
    ch1 = float(input("P1:   "))
    ch2 = float(input("P2:   "))
    ch3 = float(input("PR:   "))

    c1 = ch + ch1 + ch2
    c2 = c1 + ch3
    result = c2 / 2

    if result >= 7:
        print("Na Média:", result)
    elif result < 7:
        print("Abaixo da média:", result)

