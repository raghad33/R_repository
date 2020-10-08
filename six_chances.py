import random

index_letter = 0
print( "welcom with my game , be ready" )
count = 0
list = ['hani', 'samer', 'hoda', 'fadi']
word = random.choice( list )
# ___________________________________________________________________
def counter(inde_letter):

    inde_letter = ((inde_letter) + 1)
    return (inde_letter)
#______________________________________________________________________
while (count < 6):

    length = len( word )
    user_letter = input( "length my word {} choice the letter".format( length ) )

    if (user_letter in word):

        

        print( length )
        print( index_letter )
        if (index_letter == length):
            print( "yeeees,you are the winner" )
            break
        print( "the letter index is{} ".format( word.find( user_letter ) ) )

    else:

        print( "oooh ,you lost a chance {}".format(count) )
        count = count + 1

else:
    print( "you are out the game , bye" )

    # ___________________________________________________________________--




