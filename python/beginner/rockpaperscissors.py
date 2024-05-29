import random

pc_wins = 0
user_wins = 0

hand_choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Select your choice for playing this round: ROCK / PAPER / SCISSORS / exit ").lower()
    if user_input == "exit":
        break
    elif user_input not in hand_choices:
        print("Your choice is invalid, please try again")
    else:
        generated_random_number = random.randint(0,2)
        ### ROCK: 0, PAPER: 1, SCISSORS: 2
        pc_choice = hand_choices[generated_random_number]
        if user_input == pc_choice:
            print("You tie, try again with a new input choice for your next play!")
        else:
            for i in range(0,2):
                if user_input == hand_choices[i] and pc_choice == hand_choices[i+1]:
                    print("You lost.")
                    pc_wins += 1
                elif user_input == hand_choices[i] and pc_choice == hand_choices[i-1]:
                    print("You won.")
                    user_wins += 1
                

print(f"You won {user_wins} times")
print(f"The pc won {pc_wins} times")
print("Au revoir!")
