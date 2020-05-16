# Computer Science Final Project: "Hangman v2.0"
# Tollin Roth
# CSCI160_M01
# 5-5-2020

# DOCSTRING DIRECTIONS:
'''
Write a program that allows the user to play Hangman. You may only use techniques 
that we have covered in class. Do not use code that you find online 
that we have not covered in class, except for what is provided in this document. 

HINT: You can use two strings to manage this. One to actually hold 
the word that is being guessed and another one (of the same length) 
that will hold all the underscores and correct guesses.
'''
# IMPORTS / EXPORTS / & ODDITIES:
import os, sys, time, random

# GALLOWS STAGES START:
def display_hangman(rounds):
    # It looks backwards because I will be decrementing
    # each round that a player makes an incorrect guess
    stages = [
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         |
         ||       _/ \\_
         ||    
        ==============

        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         |
         ||       _/ \\
         ||    
        ==============

        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         |
         ||        / \\
         ||    
        ==============

        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         |
         ||        / 
         ||    
        ==============

        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         |
         ||        
         ||    
        ==============

        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|/
         ||         
         ||        
         ||    
        ==============
         
        """,
        """
          ___________
         ||         |
         ||         O
         ||        \\|
         ||         
         ||        
         ||    
        ==============
         
        """,
        """
          ___________
         ||         |
         ||         O
         ||         |
         ||         
         ||        
         ||    
        ==============
         
        """,
        """
          ___________
         ||         |
         ||         O
         ||        
         ||         
         ||        
         ||    
        ==============
         
        """,
        """
          ___________
         ||         |
         ||         
         ||        
         ||        
         ||        
         ||    
        ==============

        """,
        """
          ___________
         ||         
         ||         
         ||        
         ||         
         ||        
         ||    
        ==============
         
        """
    ]
    return stages[rounds]
# GALLOWS STAGES END:

# WELCOME FUNCTIONS START:
def welcome_mat():
    joke = '''                                                         WELCOME TO HANGMAN V2.0!!!
                                                
                                                `nM;:::::::::::::::::::::::::::::::;;*#x#@:
                                                ,Wz:::::::::::::::::::::::::::::::;;;;;iW@,
                                                `+@*:::::::::::::::::::::::::::::::;;;;;iWM`
                                                `x@i::::::::::::::::::::::::::::::::;;;;;#@:
                                                :@x:::::::::::::::::::::::::::::::::;;;;;xW.
                                               #@+:::::::::::::::::::::::::::::::::::;;;iWM`
                                            ;@x:::::::::::::::::::::::::::::::::::::::;;;*@W.
                                         @Mi::::::::::::::::::::::::::::::::::::::::::::;iiWW.
                                        Mi::::::::::::::::::::::::::::::::::::::::::::::::;;x@;
                                    M*::::::::::::::::::::::::::::::::::::::::::::::::::::::;x#:
                                 @+::::::::::::||:::||:://\\\::||\\\:::||:||=====||::::::::::;z#i
                                x@z::::::::::::||:::||:||::||:||:\\\::||:||::::::::::::::::::;#@i
                              @z:::::::::::::::||===||:||==||:||::\\\:||:||:====||:::::::::::;;*@x
                             W;::::::::::::::::||:::||:||::||:||:::\\\||:||:::::||:::::::::::;;i@W`
                            @z:::::::::::::::::||:::||:||::||:||::::\\\|:||_____||:::::::::::;;;M@.
                            @*::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;x#:
                            W;:::::::::::::::::::||\\\:://||:://\\\::||\\\::: ||:::::::::::::::;iz#
                           M:::::::::::::::::::::||:\\\//:||:||::||:||:\\\:: ||:::::::::::::::;;#@*
                          W;:::::::::::::::::::::||::::::||:||==||:||::\\\: ||::::::::::::::;;+@#`
                        .MM;:::::::::::::::::::::||::::::||:||::||:||:::\\\ ||::::::::::::::;;*@z
                        .xW;;+:::::::::::::::::::||::::::||:||::||:||::::\\\||::::::::::::::ii@x`
                        `xW;:#i::::::::::::::::::::::::::::::::::iz#;::::::::::::::::::::::;iWx`
                        `z@i:*#:::::::::::::::::::::::::;#i::::::::*ni:::::::::::::::::::::;;MW.
                        `#@*::n;:::::::::::::::::::::::::z@M+;::::::in*::::::::::::::::::::;iMW.
                        `*@+::+#:::::::::::::::::::::::::n@@@Wx#i:::::x*:::::::::::::::::::;;x@,
                        `*##::;n;:::::::::::::::::::::::*@x:+M@#@Mn#z#WWi::::::::::::::::::;;x@:
                        ;@#:::##::::::::::::::::::::::;MW;             #n::::::::::::::::::;;z@;
                        ;#z:::;ini:::::::::::::::::::;M@z`              @i:::::::::::::::::;;z#i
                      ixM@+::::::;ini:::::::::::::;i;n@:                `z@n:::::::::::::::;;x#:
                    ;;###@#:::::::::;z*:::::::::::;;;x@;                  `xW*::::::::::::;;;z@,
                   ;;ixi#@*:::::::::;+z:::::::::::;;;n#x+                 i@#:::::::::::::;;;n@, 
                  Wi;i##;z@*:::::::::;*n;::::::::::;;ix@@@.               `z@i:::::::::::::;;;WM`
                `+@#;;ixiin@*:::::::::;ini:::::::::::;;i*i*z               .Mx;:::::::::::::;;+@#`
             .MMi;;;i#+;;iWx:::::::::::;ini:::::::::::::::m*i,             @@i::::::::::::::;W@,
            *@#;;;;ini;;*@z:::::::::::;;#x#;::::::::::::::::*mi;in+;i;;;;i#M;:::::::::::::;x@+`
            `M@i;;;;*n;;;+@*:::::::::::;;+@x:::::::::::::::::::;iiiii;;;;;;ini::::::::::::z@n`
            :@Wni;;;##i;;z@;:::::::::::;;##@+:::::::::::::::::::;;;;;:::::;;zi::::::i++#n@x.
           `#Miz+;;;n*;;ix@;:::::::::::;ix#@@ni:::::::::::::::::::::::::::::#+:::::#x##+M@;`
           .Mz;z+;;ixi;;iWW;::::::::::;;*@Min@@ni:::::::::::::::::::::::::::*#::::;n;;;;xW.
           i@*ini;;#x;;;iWM:::::::::::;#W@*`.*M@@x+;::::::::::::::::::::::::;z::::*#i;;iWn`
          `xM;+#;iiWn;;;iWx:::::::::::;M@n``` `,+M@@x+;:::::::::::::::::izzzzWi:::z*;;;z@*
        ,@n;xi;;z@#;;;iWn::::::::::::+@z`      .iM#@W#;::::::::::::::+n+***##::;ni;iiWW,
        ,@xn#;;iM@*;;;iMx::::::::::::;Wx`        `:zW@Wzi::::::::::::n*ii  *M*::ni;;#@z'
        `W@xi;ix#M;;;;iMn::::::::::::;Mn`        `  .in@@M#+M@#@@@#WiWWW    @@ziM#iz@M,
        `iW@z#n@@z;;;;;xz::::::::::::;Wn`                                    M@#@@@#Wi
            :M@@@#Wi;;;;;n#::::::::::::*@z`                                    
            `:;+@zi;;;;;nz::::::::::::+@*                                                           
            `xW*;;;;;;;;;xx:::::::::::i@z`                                                                
            ,@z;;;;;;;;;;xx:::::::::::*@*                                                                 
            *@#;;;;;;;;;+@x:::::::::::#@:                                                                 
            *@Mn;;;ii;;ix#x:::::::::::nM.                                                                 
           `zWin*;i;;;;*@#M:::::::::::Mn`                                                            
             `;zxx#,`   ,WWzni::::::z@;                                                                     
                        #Wiin::::zM,                                                                     
                        *Wi*n:::#M:                                                                           '''
    for char in joke:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
def rules():
    rulebook = '''
    RULES:
    ---------------------------------------------------------------------------------------------------
    Custom Hangman v2.0 is a single player game where the 'AI' thinks of a word and 'Player One'
    Struggles to guess the word, one character at a time. The word guessed is represented by a
    Collection of dashes in a row like the following:\n
    If the word is 'cataclysmic' the player would be shown '_ _ _ _ _ _ _ _ _ _ _'\n\n

    1.) Each time you guess incorrectly, the gallows will add human appendages to it.
    6.) Once the gallows hold a completed human by the noose, the game ends and Player wins.
    0.) If Player manages to guess the word correctly, before they hang the man, then the game will
    Most definitlely end and Player wins Custom Hangman!\n
    0.) If the Player guesses the entire word early, Player wins the game!
    1.) Happy Hanging, Players...
    ---------------------------------------------------------------------------------------------------
    '''
    for letter in rulebook:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
def thank_you():
    message = '''
    CONGRATULATIONS!!!\n\
    Player, you have found my Easter Egg!\n\
    Whether it took you a while or a short amount of time...\n\
    I want you to know that I really appreciate you for taking the time to solve my puzzle.\n\
    I hope to build another one very soon.\n\n\
    Hangman v1.0 developed by 'ROTH inc.' in association with 'Boomer Industries LTD.'\n\n\
    Have a nice day! Goodbye.
    '''      
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def return_to_menu(message):
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def countdown(numbers):
    for letter in numbers:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.75)

def menu_options():
    # Build a menu
    menu = {
        "p": "Play Hangman",
        "r": "Rules",
        "q": "Quit Game"
    }
    print()
    print("MENU:")
    for key, val in menu.items():
        print("{} - {}".format(key, val))
    return menu
# WELCOME FUNCTIONS END:

# INTEGRAL FUNCTIONS START:
def load_words(file_name):
    category = {                                # Dictionary with a category of words...
        "Category": []                          # Epic Boomer Memes... lol.
    }
    file = open(file_name)                      # Function call will open the file.
    for word in file:                           # For each word in file...
        new_word = word.strip()                 # Strip each of the words by \n.
        category["Category"].append(new_word)   # Append each word to the category Category.
    file.close()                                # Close the file.
    return category
def load_ai(word):
    for word in words.values():                 # Loop through the list of words.
        ai_word = random.choice(word)           # Make the computer randomly choose a word.
    return ai_word.upper()                      # Return the random word as uppercase.
# INTEGRAL FUNCTIONS END:

# VICTORY / LOSS FUNCTIONS START:
def guesses_with_guesses():
    completion = '''
    Congratulations Champion!
    Game Over.
    '''
    for letter in completion:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
def guessed_with_word():
    completion = '''
    Congratulations Champion!
    You guessed the entire word! You Win!!!
    Game Over.
    '''
    for letter in completion:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
def ran_out_of_guesses():
    incompletion = '''
    Player ran out of guesses! You Lose.
    Game Over.
    '''
    for letter in incompletion:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
# VICTORY / LOSS FUNCTIONS END:

# HANGMAN FUNCTION START:
def hangman(word):
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen for Windows & Linux.
    welcome_mat()                                       # Roll out the welcome mat.
    menu = menu_options()                               # Assign menu variable to menu_options function.
    message = "Returning to Main Menu in: "
    numbers = "3 2 1"
    print("---------------------------------------------------------------------------------------------------")
    print()
    option = input("Choose an option: ").lower()        # Get menu choice from user.
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen for Windows & Linux.
    while option in menu:                               # Validate option and set condition
        if option == "p":                               # Begin the Verbal Carnage -- Good Luck!
            guesses = ''                                # Declare a variable to hold each guess.
            incorrect = ''                              # Create a variable to keep the correct guesses out of view.
            rounds  = 10                                # Start the rounds at 8 for decrementation.
            while rounds > 0:                   
                attempts = 0
                print(display_hangman(rounds))          # Output the Hangman stage at rounds 8.
                for letter in word:                     # Check for letter in randomly chosen word.
                    if letter in guesses:               # If the letter is correct.
                        print(letter, end=" ")          # Print the correct letter.
                    else:                               # If the letter is incorrect.
                        print("_", end=" ")             # Print an underscore instead.
                        attempts += 1                   # Increment attempts by 1.
                if attempts == 0:
                    print()   
                    print()      
                    print("The word to guess was: {}. You Win!".format(word))              
                    guesses_with_guesses()
                    return_to_menu(message), countdown(numbers)
                    os.system('cls' if os.name == 'nt' else 'clear')                # Clear the screen for Windows & Linux.
                    return
                print()
                print()
                print("Player Guesses: {}".format(incorrect))
                print("You have", rounds, "guesses left!")
                easter_egg = "CSCI160_M01".upper()                                  # A method for me to say thank you.
                guess = input("Player, guess a letter: ").upper()                   # Retrieve uppercase guess from user.
                if guess == word:
                    print()
                    print("The word to guess was: {}.".format(word))                # Check to see if the guess is the word.
                    guessed_with_word()
                    return_to_menu(message), countdown(numbers)
                    os.system('cls' if os.name == 'nt' else 'clear')                # Clear the screen for Windows & Linux.
                    return
                elif guess.isalpha() and len(guess) == 1 and guess in word:         # Validate user guess if in word.
                    guesses += guess + " "                                          # Add correct guess to guesses.
                elif guess.isalpha() and len(guess) == 1 and guess not in word:     # Validate user guess if not in word.
                    incorrect += guess + " "                                        # Add incorrect guess to incorrect.
                else:
                    rounds -= 1
                os.system('cls' if os.name == 'nt' else 'clear')                    # Clear the screen for Windows & Linux.                                          
                if guess not in word:                                               # If guess is not equal to a letter in word.
                    rounds -= 1                                                     # Decrement rounds by 1.
                    print("Incorrect Guess")                                        # Visualize the 'Incorrect Guess'
                    if rounds == 0:                                                 # Game Over, if player ran out of rounds
                        print()
                        print("The word to guess was: {}.".format(word))  # Share the word with user.
                        ran_out_of_guesses()
                        return_to_menu(message), countdown(numbers)
                        os.system('cls' if os.name == 'nt' else 'clear')            # Clear the screen for Windows & Linux.
                        return
                if guess == easter_egg:
                    os.system('cls' if os.name == 'nt' else 'clear')                # Clear the screen for Windows & Linux.
                    thank_you()
                    return
        elif option == "r":                                                 
            os.system('cls' if os.name == 'nt' else 'clear')                        # Clear the screen for Windows & Linux.    
            rules()             
            print()
            menu_options()      
            print()
            option = input("Choose an option: ").lower()    
            os.system('cls' if os.name == 'nt' else 'clear')                        # Clear the screen for Windows & Linux.                                
        elif option == "q":
            os.system('cls' if os.name == 'nt' else 'clear')                        # Clear the screen for Windows & Linux.
            goodbye = "Goodbye, my love..."
            for letter in goodbye:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.015)
            quit()
# HANGMAN FUNCTION END:

# MAIN PROGRAM START:
def main():
    word = load_ai(words)                                   # Assign a random word to word variable.
    for value in words.values():
        if word == value:
            del value
    hangman(word)                                           # Run the Hangman program.
    start_menu = "Y"                            
    while start_menu == "Y":                                # Create a loop for replaying the game.
        word = load_ai(words)                               # Assign a new random word to word variable.
        hangman(word)                                       # Replay the Hangman program.
        os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen for Windows & Linux.
# MAIN PROGRAM END:

# MAIN FUNCTION CALL:
if __name__ == "__main__":
    words  = load_words("words.txt")                # Open 'words.txt' and access a list of words.
    main()
