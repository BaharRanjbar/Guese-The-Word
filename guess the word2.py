import random
list_of_words = []

def get_input():
    while True:
        user_input = input("Enter word: ")
        if user_input.isalpha():
            return user_input.lower()
        print("User input isn't correct. PLEASE ENTER AGAIN!") 

def input_list():
    while True:
        user_input = get_input()

        while user_input != "done":
            list_of_words.append(user_input)        
            user_input = get_input()
        
        return list_of_words
       
def get_input_from_list(words):
    user_input = get_input()
    while user_input not in words:
        print("you should guess a word from the given words list")
        print("Please enter a correct word.")
        user_input = get_input()
        
    return user_input

def print_game_intro():
    print("Hi, Welcome to the Guess Game")
    print("All words:", list_of_words)
    print("Please start guessing.")
    
def run_game(number_of_rounds , words):
    print_game_intro()
    print(f"number of guesses: {number_of_rounds}")
    correct_word =random.choice(words)
    
    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)
        
        if user_input == correct_word:
            print("YOU WON!")
            return
        else:
            print("you guess wrong")
            print(f"please try again!number of rounds left: {number_of_rounds-1-i}")
            
    print("you are a looser!")



input_list()
run_game(5 , list_of_words)












         

