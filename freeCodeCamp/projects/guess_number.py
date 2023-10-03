import random

random_num = random.randint(1, 200)

def guess_num(x):
    if random_num < x:
        print("Es un numero mas pequeño")
    elif random_num > x:
        print("Es un numero mas grande")
    elif (random_num == x):
        print("======= WINNER ========")
        print(f"El numero adivinado es {random_num}")
        return False
        
while True:
    x = int(input("Quer numero quieres introducir: "))
    print(x)
    if guess_num != False:
        guess_num(x)
    else:
        break