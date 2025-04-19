import random   # to generate random choices for the computer

# using global variables to keep track of scores across various function calls
userWin = 0
computerWin = 0
ties = 0

# Function to validate user input
def UserChoiceValidate(user_choice):
    valid_choices = ['rock', 'paper', 'scissors']
    if user_choice not in valid_choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return False
    return True

# Function to determine the winner and update scores
def FindWinner(user_choice, computer_choice):
    global userWin, computerWin, ties
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        userWin += 1
    else:
        print("Computer wins!")
        computerWin += 1

# Function to play the game
def RockPaperScissor(n):
    # first round will have no quit option
    if(n==0):
        user_choice= input("Enter your choice: ").lower()
        # Validate user choice
        if not UserChoiceValidate(user_choice):
            print("Please try again.")
            RockPaperScissor(n)
            return
        # computer will randomly choose one of the three options
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        FindWinner(user_choice, computer_choice)
        n += 1
        RockPaperScissor(n)
        return  #to prevent it from going to the next line, completely exit the function
    
    print("Press ENTER if you wish to play another round")
    user_command = input("OR enter 'Quit' if you wish to end the game: ").lower()
    # validate user command
    if user_command not in ['quit', '']:
        print("Invalid command! Please press ENTER or enter 'Quit'.")
        RockPaperScissor(n)
        return
    if user_command == 'quit':
        # all the result is being printed here once the game ends
        print("Thanks for playing!")
        print(f"Total rounds played: {n}")
        print(f"User wins: {userWin}")
        print(f"Computer wins: {computerWin}")
        print(f"Ties: {ties}")
        return 
    # if quit is not chosen
    user_choice= input("Enter your choice: ").lower()
    # Validate user choice
    if not UserChoiceValidate(user_choice):
        print("Please try again.")
        RockPaperScissor(n)
        return
    # computer is randomly choosing one of the three options
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    FindWinner(user_choice, computer_choice)
    n += 1
    RockPaperScissor(n)


# the main body of the program, where the game starts
print("Welcome to the Rock Paper Scissors Game!")
n = 0   # chances played upto now(initially 0)
# calling the function to start the game
RockPaperScissor(n)