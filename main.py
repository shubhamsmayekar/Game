import random

word_list = ["aardvark", "baboon", "camel"]

print(r'''Lets play  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
wrong_guess = 0
game_over = False

while not game_over:
    print(f"\nWord: {' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        wrong_guess += 1
        print(f"Wrong guess! Lives remaining: {6 - wrong_guess}")
        
        if wrong_guess == 1:
            print(r'''  
               _______
             |/      |
             |      (_)
             |      
             |       
             |     
             |
          ___|___''')
        elif wrong_guess == 2:
            print(r'''    
                _______
             |/      |
             |      (_)
             |       |
             |       
             |     
             |
          ___|___''')
        elif wrong_guess == 3:
            print(r'''    
               _______
             |/      |
             |      (_)
             |      \|
             |       
             |       
             |
          ___|___''')
        elif wrong_guess == 4:
            print(r'''    
               _______
             |/      |
             |      (_)
             |      \|/
             |       
             |       
             |
          ___|___''')
        elif wrong_guess == 5:
            print(r'''    
               _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |       
             |
          ___|___''')
        elif wrong_guess == 6:
            print(r'''    
               _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / \
             |
          ___|___''')
            print("\nGame Over! You lost!")
            print(f"The word was: {chosen_word}")
            game_over = True

    if "_" not in display:
        print("\nCongratulations! You won!")
        print(f"The word was: {chosen_word}")
        game_over = True