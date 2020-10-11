import random


# function produces the random number
def GuessNum():

    my_num = random.randint(0,100)

    return my_num

#the main function

def main():

    the_number = GuessNum()


#the main conditions

    while (the_number<100):


        print("enter the choice number \n")
        your_number = int(input())


        if (your_number == the_number):

            print("yeeeees, nice")
            break

        elif (your_number < the_number):

            print(" give me bigger number ")

        else:
            print("give me smaller number")

    else:
        print("out the range")

if __name__ == '__main__':main()