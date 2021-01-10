# Word or Number guessing game (2018)

import random #to generate random words and numbers

def guess_number(generated):
    """(int)-> void

    This function evaluates generated (int) against the user's guess (int) to
    determine whether the user has correctly guessed the random number.
    
    >>> guess_number(3)
    Enter you guess:2
    Too low. Try again.
    Enter you guess:4
    Too high. Try again.
    Enter you guess:12
    You have to guess a number of 1 digits. Try again!
    Enter you guess:3
    Good job!The number is 3 .
    """
    while True:  
        guess=int(input("Enter you guess:")) #user's guess
        
        if len(str(guess))==len(str(generated)): #make sure the guess is of correct length
        
            # evaluate the guess
            if guess>generated:
                print("Too high. Try again.")
            elif guess<generated:
                 print("Too low. Try again.")
            else:
                print("Good job!The number is", guess,".") 
                break #will stop the current while loop
        else:
            print("You have to guess a number of {} digits. Try again!".format(len(str(generated))))       
    
def guess_word(generated): 
    """(str)-> void

    This function evaluates generated (str) against the user's guess (str) to
    determine whether the user has correctly guessed the random word.
    
    >>> guess_word("cat")
    The word has 3 letters.
    __ __ __ 
    You have 9 tries. Good luck!

    Enter a letter guess:i
    Wrong guess. You have 8 tries left.
    __ __ __ 

    Enter a letter guess:c
    Good job. You have 7 tries left.
    ['c', 'a', 't']
    c __ __

    Enter a letter guess:c
    Good job. You have 6 tries left.
    ['c', 'a', 't']
    c __ __

    Enter a letter guess:a
    Good job. You have 5 tries left.
    ['c', 'a', 't']
    c a __

    Enter a letter guess:1
    Wrong guess. You have 4 tries left.
    c a __

    Enter a letter guess:t
    Good job. You have 3 tries left.
    ['c', 'a', 't']
    c a t
    Congratulations! You have correctly guessed the word.
    Game over!
    """
    print( "The word has {} letters.".format(len(generated))) #inform the user of the length
    
    picture="__ " * len(generated) #pictorial representation of the guessing progress
    print(picture)
    
    keep=[] # initalize a list of correctly guessed letters
    
    #limit the number of tries to 3 times the length of the word
    remaining_guess=3*len(generated)
    
    print("You have {} tries. Good luck!".format(remaining_guess))#inform the user of attempts available
    
    while remaining_guess>0: 
        attempt=input("\nEnter a letter guess:").lower() #user's guess
        
        if attempt in generated: #if user guessed a correct letter
            keep.append(attempt) #add guess to list of correct attempts 
            remaining_guess-=1 
            print("Good job. You have {} tries left.".format(remaining_guess))
            
            #The following code is to update the pictorial representation
            word_as_list=list(generated)
            for letter in word_as_list: #for each letter in the generated word
                if letter!=attempt and (letter not in keep):#if the letter has not already been guessed correctly and if it's not the currently guessed letter
                    index = word_as_list.index(letter)
                    word_as_list[index]= "__"  #then we replace the letter with __
                    
            updated_picture=" ".join(word_as_list) #convert to string and print
            print(updated_picture)
            
            if "__" not in word_as_list: #if all the letters have been guessed
                    print("Congratulations! You have correctly guessed the word.")
                    break
                
        else: #if user guessed wrong 
            remaining_guess-=1
            print("Wrong guess. You have {} tries left.".format(remaining_guess))
            
            # update the pictorial representation of the guessing progress
            if len(keep)==0: # no correctly guessed letters yet
                print(picture)
                
            else: # user has previously guessed a letter inside the generated word
                print(updated_picture)
                
    if remaining_guess==0: 
        print("Game over!")#if all chances have been used, the program will return to the main menu
    
#_________________________________________________________dictionaries of words_________________________________________________________

list_of_fruits={
1:"apple",2:"apricot",3:"avocado",4:"banana",5:"blackberry",
6:"blueberry",7:"cantaloupe",8:"cherry",9:"clementine",10:"cranberry",
11:"grapefruit",12:"grape",13:"jackfruit",14:"kiwi",15:"lemon",
16:"mango",17:"orange",18:"papaya",19:"peach",20:"pear",
21:"pitaya",22:"pineapple",23:"plum",24:"pomegranate",25:"raspberry",
26:"strawberry",27:"tangerine",28:"watermelon"}

list_of_animals={
1:"lion",2:"shark",3:"eagle",4:"goat",5:"bear",
6:"rat",7:"mouse",8:"horse",9:"bird",10:"llama",
11:"elephant",12:"tiger",13:"monkey",14:"panda",15:"pig",
16:"cow",17:"fox",18:"lynx",19:"fish",20:"python",
21:"frog",22:"jaguar",23:"cheetah",24:"wolf",25:"penguin",
26:"zebra",27:"rabbit",28:"giraffe",29:"koala",30:"kangaroo",
31:"sheep",32:"deer",33:"chicken",34:"owl",35:"turtle"}

list_of_countries={
1:"algeria",2:"argentina",3:"australia",4:"austria",5:"bangladesh",
6:"belgium",7:"bhutan",8:"bolivia",9:"brazil",10:"canada",
11:"chile",12:"china",13:"colombia",14:"croatia",15:"cuba",
16:"denmark",17:"ecuador",18:"egypt",19:"france",20:"germany",
21:"greece",22:"hungary",23:"india",24:"iran",25:"israel",
26:"italy",27:"japan",28:"korea",29:"laos",30:"malaysia",
31:"mexico",32:"mongolia",33:"myanmar",34:"netherlands",35:"norway",
36:"peru",37:"portugal",38:"poland",39:"russia",40:"spain",
41:"sweden",42:"turkey",43:"uganda",44:"vietnam",45:"zimbabwe"}

#______________________________________________________________________________________________________________________________________

def main():
    """()-> void

    This function displays the menu and calls guess_number() or guess_word() if needed.
    
    >>> main()
    GUESS THE WORD OR NUMBER!
                  ***Main Menu***
                  I want to guess a [A] number [B] word
                  Chose an option by entering the corresponding letter or [C] to exit the game: a

    GUESS THE NUMBER~
                                  Chose a number length: [1] digit [2] digits [3] digits [4] digits
                                  Enter the corresponding number or [5] to return to main menu:
    Oups! Your choice is invalid.

    GUESS THE NUMBER~
                                  Chose a number length: [1] digit [2] digits [3] digits [4] digits
                                  Enter the corresponding number or [5] to return to main menu:
    """
    
    while True: 
        choice=input("""\nGUESS THE WORD OR NUMBER!
                  ***Main Menu***
                  I want to guess a [A] number [B] word
                  Chose an option by entering the corresponding letter or [C] to exit the game: """)

        choice1=choice.upper()

        if choice1=="A": #number guessing name
            while True:
                choice2=input("""\nGUESS THE NUMBER~
                              Chose a number length: [1] digit [2] digits [3] digits [4] digits
                              Enter the corresponding number or [5] to return to main menu:""")
                if choice2=="1":
                    number=random.randint(0,9) #generate number between 0 and 9
                    guess_number(number) #calling the previously defined guess_number() function
                    
                elif choice2=="2":
                    number=random.randint(10,99)
                    guess_number(number)
                    
                elif choice2=="3":
                    number=random.randint(100,999)
                    guess_number(number)
                    
                elif choice2=="4":
                    number=random.randint(1000,9999)
                    guess_number(number)
                    
                elif choice2=="5": #breaks the current while loop and returns to main menu 
                    break
                
                else: #limits the entry format to integer 1,2,3,4 or 5
                    print("Oups! Your choice is invalid.")
                    
        elif choice1=="B": #word guessing 
            while True:
                choice3=input("""\nGUESS THE WORD~
        Chose a word category: [1] fruit [2] animal [3] country
        Enter the corresponding number or [4] to return to main menu:""")
                
                if choice3=="1":
                    word=random.choice(list_of_fruits) #generate random word from corresponding list
                    guess_word(word) #calling the previously defined guess_word() function
                    
                elif choice3=="2":
                    word=random.choice(list_of_animals)
                    guess_word(word)
                    
                elif choice3=="3":
                    word=random.choice(list_of_countries)
                    guess_word(word)
                    
                elif choice3=="4": #the input being 4 will end the current while loop and return to the main menu 
                    break
                
                else:#limits the input to 1,2,3 or 4
                    print("Oups! Your choice is invalid.")

        elif choice1=="C": #will break the first while loop and stop the program
            print("Goodbye!")
            break

        else:
            print("Oups! Your entry is invalid. You must choose between options A, B and C.") #Informs user of entry error

if __name__ == '__main__':
    main()