

def main():
    # this is a comment, it is not code, just a note
    # storing data with variables 

    a = 1 # store the value 1 into 'a', now 'a' "is" 1
    print(a) # prints 1

    # operations
    number = 5 # number equals 5
    number = 5 + 2 # number equals 7
    number = 5 - 2 # number equals 3

    # operators are applied between two types of data (take note this is important):
    # the common operators are as follows: 
    # [+ for addition], [- for subtraction], [* for multiplication], [/ for division], [** for exponentiation]
    # note that division has some weird behaivior, but we don't have time to go over it so if you're curious 
    # you can look up "integer division vs floating division python"

    b = "hi there" # this scores the text "hi there" into 'b'
    print(b) # prints hi there

    if a == 1: # two equal signs check equality rather than assign a variable
        print("yes, a is equal to one") # code tabbed in after the ':' is only run if this is true

    # outside the if statement, code here is run reguardless of if the if statement was true

    text = input("Please type something: ") # get input from whoever is running the program
    print("You typed: " + text) # prints out a message saying what you typed in


    for i in range(5): # this is a loop, code here is run 5 times (each time the variable 'i' goes up [0, 1, 2, 3, 4])
        print(i) # prints 0, 1, 2, 3, 4 (counting in code starts at 0)

    print("---------") # seperator to make the output more clear
    test_array = [1, 4, 5, 2, 3, 1, 9, 12, 5] # this is an array.  It is basically a list of numbers stored in one variable
    # you can loop over each element in this list in a similar way to the previous loop
    for number in test_array: # number is equal to each element in the array at each iteration 
        print(number) # prints 1, 4, 5, 2, 3 ... ect

    # now lets combine loops and if statements 
    print("---------") # seperator to make the output more clear
    for number in test_array: # loops over each number 
        if number % 2 == 0: # '%' is remainder division (basically this checks if the number is even)
            print(number) # if the number is even, print it
        

if __name__ == "__main__": # ignore this, it is completely unimportant to the code we are learning
    main()