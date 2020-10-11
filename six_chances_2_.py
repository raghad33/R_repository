
import random
import re

index_letter = 0# initialize value to count the correct letters
print( "welcom with my game , be ready" )
count = 0 # initialize value to count the incorrect values

list = ['optimise', 'success', 'sky', 'university']
word = random.choice( list )# a random choice function to choice a word from the list

#some definations about the words
if (word == 'optimise'):
    print("if you want to be better you own an _ _ _ _ _ _ _ _:")
elif(word == 'success'):
    print("if you work hardly you will _ _ _ _ _ _ _")
elif(word == "sky"):
    print("its very high _ _ _")
else:
    print("a place to study _ _ _ _ _ _ _ _ _ _")

my_word = ['_','_','_','_','_','_','_','_','_','_']
# ___________________________________________________________________
# a counter function
def counter(inde_letter):

    inde_letter = ((inde_letter) + 1)
    return (inde_letter)

# ______________________________________________________________________
#def find_letter(X):
#    for letter in word:
#        Y=word.find(X)
#        return Y

# ______________________________________________________________________
#the main program body
while (count < 6):

    length = len( word )
    user_letter = input( "length my word {} choice the letter".format( length ) )#ask user to input letter
#if the input letter is correct ,find index
    if (user_letter in word):
        index_input_letter = [m.start() for m in re.finditer( user_letter, word )]
        # return item from duplicate items list
        for the_index in index_input_letter:
            index_my_word = the_index
            my_word[index_my_word] = user_letter
            print(my_word)

        #return  duplicate item sum
        indexes = len(index_input_letter)

        if (indexes > 1):
            index_letter = counter(index_letter) + (indexes - 1)
            print('index_letter' ,index_letter)
        else:
            index_letter= counter(index_letter)

        print( "the letter index is{} ".format( index_input_letter ) )

        if ((index_letter) == length):
            print("yeeees,you are the winner  \n, my word is {} ".format(word))
            break


    else:
        print("oooh ,you lost a chance {} ".format(count))
        count = count + 1

else:
    print("you are out the game , bye")

    # ___________________________________________________________________--




