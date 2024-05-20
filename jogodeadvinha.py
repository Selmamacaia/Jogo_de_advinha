import random
import time

numero_secreto = random.randint(1, 100)
tentativas = 5

time.sleep(3)
print('start game|_|')
time.sleep(3)
print('esse é um jogo de advinha, você tem 5 chances para acertar o numero...')
time.sleep(3)
while tentativas > 0:
   
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    if palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
    elif palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    else:
        print("Parabéns! Você adivinhou o número!")
        break
    tentativas -= 1  
    if tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes.")
    else:
        print("Você não tem mais tentativas. Game over.")

if tentativas == 0:
    print(' game over...')
    print(f'o numero secreto era: {numero_secreto}')

