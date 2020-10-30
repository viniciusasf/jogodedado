from cv2 import cv2
import sys
from random import randint

p = "S"
while True:
    p = input("Vamos iniciar o Jogo? Digite [S]-SIM / [N]-Não: ").upper()
    if p == "S":
        print("\nIniciando o Jogo de Dados... ")
        print("Jogue o dado a primeira vez: PRECIONE ENTER")
        input()
        a = randint(1, 6)
        print("Jogue o dado a segunda vez: PRECIONE ENTER ")
        input()
        b = randint(1, 6)
        print("Jogue o dado a terceira vez: PRECIONE ENTER ")
        input()
        c = randint(1, 6)
        d = (a+b+c)
        break

    elif p == "N":
        print("OBRIGADO, PROGRAMA ENCERRADO")
        sys.exit()

    elif p != "S" or "N":
        print("\n\nALERTA: Digite S ou N: \n")

c = 0
while True:
    for i in range(4, -1, -1):
        print(f"Voce tem {i} chances")
        x = int(input("Adivinhe o Valor Total das 3 jogadas, digite aqui: "))
        c += 1
        if c == 5:
            print("FIM DO JOGO, Suas Chances Acabaram... ")
            input()
            sys.exit()

        elif x > 19:
            print("\nO valor é muito Alto, diminua o valor")


        elif x <= 3:
            print("\nValor impossivel, devido cada dado conter o mínino 1 de valor, escolha numero maior que 3")


        elif x > d:
            print("\nDiminua o Valor: ")


        elif x < d:
            print("\nAumente o Valor")


        elif x == d:
            im = cv2.imread("acerto.jpg", 0)
            cv2.imshow("image", im)
            cv2.waitKey(5)
            cv2.destroyWindow("image")