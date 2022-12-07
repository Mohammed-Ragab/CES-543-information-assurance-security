import random
import string
import sys
# note:  sys.argv[0] has the name of the python file
length = int(sys.argv[2]) #number of iteration which represents also the length of the output string
seed_value = int(sys.argv[1]) #seed input from command line, it helps us to get the same output from any random function in Random module in python such as "random.choice()". if seed value changes, you will get different random string for the same length

#  prog_0 was crashed with seed 2 and number of iteration 100
#  prog_1 was crashed with seed 2 and number of iteration 100
#  prog_2 was crashed with seed 2 and number of iteration 300
#  prog_3 was crashed with seed 2 and number of iteration 300 
#  prog_4 was crashed with seed 2 and number of iteration 300
#  prog_5 was crashed with seed 2 and number of iteration 300 
#  prog_6 was crashed with seed 2 and number of iteration 300 
#  prog_7 was crashed with seed 2 and number of iteration 300 
# prog 8, I could not be able to crash it, I always get "Reading too much!" output
# prog_9 was crashed with seed 3 and number of iteration 300


''' # test that we got the commandline argument
print("seed number is " , seed_value)
print("number of iteration is ", length) '''

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.printable # " string.printable"  is a constant which contains all printable ASCII characters including upper and lower letter, digits, and special characters and space characters
    random.seed(seed_value) # setting a seed value to a random function in python makes sure that any function in the random module outputs(i.e generates) the same output (i.e random.choice(letters) generates the same output when given the seed value) , this is called "Deterministic output"
    result_str = ''.join(random.choice(letters) for i in range(length)) #random.choice(letters) function is executed length(i.e number of iterations) of times, so that number of iterations is the length of the generated string
    print(result_str)

#call function to print on standard output(i.e terminal)
get_random_string(length)

''' # test that we get the same ouput string of our program (fuzzer) givien the same seed value (i.e deterministic behaviour)
get_random_string(length)
get_random_string(length) '''