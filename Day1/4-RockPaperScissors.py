import random

print("Welcome to a Rock Paper Scissors game.")
player_choice = int(input("For Rock type 1, for Paper type 2 and for Scissors type 3. Your choice is: "))
cpu_choice = random.randint(1,3)

if (player_choice == 1):
    player_hand = "Rock"
elif (player_choice == 2):
    player_hand = "Paper"
else:
    player_hand = "Scissors"
if (cpu_choice == 1):
    cpu_hand = "Rock"
elif (cpu_choice == 2):
    cpu_hand = "Paper"
else:
    cpu_hand = "Scissors"

print(f"You chose {player_hand} and CPU chose {cpu_hand}")
if player_choice == cpu_choice:
    print("Draw. Nobody Wins")
elif (player_choice == 1 and cpu_choice == 3) or (player_choice == 2 and cpu_choice == 1) or (player_choice == 3 and cpu_choice ==2):
    print("Player Wins")
else:
    print("CPU Wins")