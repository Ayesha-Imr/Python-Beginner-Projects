import random
from english_words import english_words_lower_alpha_set

#generating a random word from the set of lower case words, not containing spaces or hyphens
myWord=random.choice(list(english_words_lower_alpha_set))

#initializing an empty "dashed" list equal to the length of the selected word, it will store correctly guessed letters
guess=[]
for i in range(len(myWord)):
    guess.append("_")
print(guess)

#creating variable to store number of tries
tries=0

#creating a set to store all the previously guessed words so player can keep track of them
done=set()

#creating loop to keep asking for a letter as input until the entire word has been guessed
while "_" in guess and tries < 10:
    # taking a letter as input
    letter = input("Enter a letter: ").lower()
    done.add(letter)
    tries+=1
    print(letter)
    if letter in myWord:
        #if the input letter is correct, then access its position in the word
        pos = myWord.index(letter)
        #set a boolean variabke to determine whether there is an empty space for that letter i.e it has not already been entered
        exists=True
        while guess[pos]!="_" and exists:
            try:
                #keep accessing next position of the repeated letter in word until its position in the guess list is not empty
                pos = myWord.index(letter, pos + 1, len(myWord) + 1)
            except:
                #if no other position of repeated letter remains, set boolean variable to false so that searh stops
                exists=False
        if exists==True:
            #if empty space for the letter exists in the guess list, then put the letter in that position
            guess[pos]=letter
            #if letter is correct, then we will add to tries so subtract 1 from tries as it is being incremented automatically at
            #the beginning of the while loop
            tries-=1
            print(guess)
            #if there are letters left to guess then display the following messages displaying info, else display Congrats message
            if "_" in guess:
                print("Letters that you have entered uptil now are", done, "." )
                print("You now have " + str(10-tries) + " tries left.")
            else:
                print("Congrats! You guessed the word correctly!")
        else:
            print("Sorry, you already guessed this letter and it does not occur again in the word.")
            print(guess)
            print("Letters that you have entered uptil now are", done, ".")
            print("You now have " + str(10 - tries) + " tries left.")
    else:
        print("Wrong guess. Letter not present in the word.")
        print(guess)
        print("Letters that you have entered uptil now are", done, ".")
        print("You now have " + str(10 - tries) + " tries left.")
if tries == 10:
    print("Oops! You ran out of tries! Better luck next time. The word was " + myWord.lower() + ".")




