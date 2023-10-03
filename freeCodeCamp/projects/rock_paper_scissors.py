import random


def play(arr_game):
    player1 = 0
    player2 = 0
    for game in arr_game:
        print(game)
        after_player1= player1
        for play in winners:
            if game == play:
                player1 += 1
                break
            elif game[0] == play[0] and game[1] == play[1]:
                continue
        if after_player1 == player1:
            player2 += 1
    if player1 > player2:
        winner = f"Player1 con {player1} puntos\n"
    elif player1 == player2:
        winner = "Empate"
    else:
        winner= f"Player2 con {player2} puntos\n"
    print("=====WINNER=====")
    print(f"El ganador es: {winner}")
    return True
    
winners = [
    ["🪨","✂️"],
    ["📋","🪨"],
    ["✂️","📋"]
]

arr_game = []
while True:
    player = input("Que quieres sacar: ")
    ordenador = random.choice(["✂️","🪨","📋"])
    if arr_game == []:
        arr_game = [player + ordenador]
    else:
        arr_game.append([player + ordenador])
    print(len(arr_game))
    
    if len(arr_game) > 3:
        res = False
        res = play([arr_game])
        if res == True:
            break
