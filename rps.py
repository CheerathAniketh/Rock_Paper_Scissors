import random

def rps():
  print("Welcome to Rock-Paper-Scissors!\n")

  rounds = int(input("How many times do you want to play \n"))

  print("Instructions: Type Rock, Paper, or Scissor and press Enter.\n")

  options =['ROCK', 'PAPER', 'SCISSOR']



  for i in range(rounds):
    computer = random.choice(options)


    player = input("Your Move? Type Rock Paper Scissor\n ")

    player_move = player.upper()


    print("Your move is", player_move)
    print("The computer move is", computer)

    if player_move == computer:
      print("Oh damn it's a tie, run this code again to play again ")
      #print("To play this game again enter Ctrl + shift") this step is for notebook users 
      break
    elif player_move == 'SCISSOR' and computer == 'ROCK':
      print("Computer Wins")
    elif player_move == 'ROCK' and computer == 'PAPER':
      print("Computer Wins")
    elif player_move == 'PAPER' and computer == 'SCISSOR':
      print("Computer Wins")
    else:
      print("You win!")

rps()
