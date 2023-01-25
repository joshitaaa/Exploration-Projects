#Pictures used in the Game
import random, sys
hangman_pics = [r"""
+--+--+
|  |  |
|     |
|     |
|     |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
|     |
|     |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
|  |  |
|     |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
| /|  |
|     |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
| /|\ |
|     |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
| /|\ |
| /   |
|     |
=======""",
r"""
+--+--+
|  |  |
|  0  |
| /|\ |
| / \ |
|     |
======="""]

CATEGORY_1 = "Fruits"
Words_1 = 'APPLE ORANGE PINEAPPLE PEAR GRAPE BANANA PERSIMMON WATERMELON PLUM CHERRY KIWI PAPAYA AVOCADO DURIAN FIG GUAVA LONGAN MANGO PEACH LEMON '.split()

CATEGORY_2 ="Animals"
Words_2 = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

CATEGORY_3 = "Occupation"
Words_3 = 'DOCTOR CARPENTER PILOT ASTRONAUT ARCHITECT PAINTER DETECTIVE CHEF ACTOR PHOTOGRAPHER LAWYER ENGINEER PLUMBER TEACHER SCIENTIST STUDENT ACCOUNTANT ENTREPENEUR POLICEMAN FIREFIGHTER POLITICIAN NURSE CLEANER TECHNICIAN SECRETARY DENTIST MECHANIC WAITER TAILOR SINGER JOURNALIST ATHLETE VETERINARIAN POSTMAN FLORIST DESIGNER HAIRDRESSER SOLDIER LIBRARIAN FARMER BOTANIST'.split()
def menu():
    print("""
    Welcome to the game of hangman!!
    Here are the categories to choose from:
    CATEGORY_1:  Fruits
    CATEGORY_2:  Animals
    CATEGORY_3:  Occupation

    To select a category, please enter the number of the category you choose
    """)
    #Allowing users to choose a category
    global chosenCategory, word, ChosenCat
    chosenCategory = input("Enter your desired category as 1,2 or 3:")
    if chosenCategory.isdigit() and int(chosenCategory) > 0 and int(chosenCategory) <=3:
        if chosenCategory == '1':
            word = Words_1
            ChosenCat = "Fruits"
        elif chosenCategory == '2':
            word = Words_2
            ChosenCat = "Animals"
        elif chosenCategory == '3':
            word = Words_3
            ChosenCat = "Occupation"
    missedLetters = []
    correctLetters = []
    secretWord = random.choice(word)

    while True: #Main game loop
        drawHangman(missedLetters, correctLetters, secretWord)
        guess = getPlayerGuess(missedLetters + correctLetters)
        #Adding correct letters to the correctLetters list
        if guess in secretWord:
            correctLetters.append(guess)
            foundAllLetters = True # Assuming you have won
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:#If there is a letter in the secret word not in the correctLetters, no win yet
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print("You got it!")
                print("YOU WON!")
                break #Exit main game loop since they won
        else:
            missedLetters.append(guess) # Add wrong letters to the missedLetters list
            if len(missedLetters) == len(hangman_pics)- 1:#Excluding the first picture
                drawHangman(missedLetters, correctLetters, secretWord)
                print("You have run out of guesses")
                print("The secret word was {}".format(secretWord))
                break

def drawHangman(missedLetters, correctLetters, secretWord):
    print(hangman_pics[len(missedLetters)])
    print("The Category is {}".format(ChosenCat))
    print()

    print("Missed Letters: ", end = '')
    for letter in missedLetters:
        print(letter, end = '')
    if len(missedLetters) == 0:
        print("No missed letters yet.")
    print()

    blanks = ['_ '] * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]
    print(''.join(blanks))

def getPlayerGuess(alreadyGuessed):
    while True:
        print('Guess a letter:')
        guess = input('>').upper()
        if len(guess) !=1:
            print("Please enter a single letter!")
        elif guess in alreadyGuessed:
            print("You have already guessed this letter!")
        elif not guess.isalpha():
            print("Please enter an alphabet!")
        else:
            return guess

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit()
