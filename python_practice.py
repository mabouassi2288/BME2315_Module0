# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

#name: Mona Abou-Assi 
#year: 2
#class: BME 2315
#USE OF AI: asked AI to verify that my "N = int(input variable by user)" was properly written

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments

N = int(input variable by user) //creates the input variable that the user types in

If N <= 0 // if the user inputs the number 0
    then return 0 // returns 0 if the first number is equal or less than 0

If N = 1 // if the user inputs the number 1
    then return 0 // the first number of the fibonacci sequence is 0, so it should return 0

set a = 0 // this is the first number of fibonacci sequence
set b = 1 // this is the second number of fibonacci sequence
set count = 0 //sets the count, which is how many times the cycle iterates
set sum = 0 //this will be the final sum, it changes as you go through each iteration

If N >= 2 // if the user inputs an N value greater than or equal to 2
    sum = a + b // sets up the sum to be a + b in the first place
    while count < N //makes a while loop for as long as the count has gone through iterations before N
        a = b //moves a to b 
        b = a + b //moves b to the next number in fibonacci sequnces
        sum = sum + b//sets sum equal to the most updated b value

        count = count + 1 //updates the count for iterations, so we can stop when we reach N

set print = sum //prints the sum when we're finished iterating 


"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 #sets N value to initial condition, which is 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # this is what controls how many times the while loop occurs
total = 0 #this is going to be our final answer

while count < N:
    #total = total + b // the problem is that the adding b to the total means it runs one extra time and actually adds the 7th term instead of stopping at the 6th term
    total = total + a #this ensures that the total being added stops at the 6th number, which is depicted with a

    next_value = a + b #this makes the next value for b
    a = b #this moves along the fibonacci sequence
    b = next_value 

    count = count + 1

print(total) #prints out our answer (should be 12)

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np #imports numpy so we can use the library for the standard deviation

data = [0,1,1,2,3,5,8,13,21,34] #makes a list of data
calculation = np.std(data) #calculates the standard deviation of the first 10 figures of the fibonacci sequence

print("Your standard deviation is: " + calculation)


# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

#USED AI: to inform me how to add a number to a list in a while loop (code on line 109)

N = 5 #sets the starting variable for the fibonacci sequence

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 #same as problem 2
total = 0 #same as problem 2
N_count = 0 #this is the count for how many times we will run through the N while loop, which will be six times
final_answer = [] #this is the list of values that needs to be filled
stop = 6 #this is when we need to stop the outer while loop

while N_count < stop: #this ensures that the outer loop will stop at N = 30

    while count < N: #same while loop as problem 2
        total = total + a #this ensures that the total being added stops at the 6th number, which is depicted with a

        next_value = a + b
        a = b
        b = next_value 

        count = count + 1


    final_answer.append(total) #this adds the value to our final answer in list format every time the N while loop is finished

    N = N + 5 #this accounts for the next N value 
    N_count = N_count + 1 #this contributes to the outer while loop
    total = 0 #resets the total so it can accurately do the fibonacci sequence on the next N number
    count = 0 #resets the count 



print(final_answer)


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #took off the quotation marks to address TypeError in line 142
    b = 1 #took off the quotation marks to address TypeError in line 142
    index = 0 #added to fix the NameError

    while a <= limit: #//TypeError: a and b are created as strings, when they should be integers
        next_value = a + b
        a = b
        b = next_value
        index += 1 #NameError: index was not defined, fixed in line 140

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".

def sum_even_fib(limit):
    a, b = 0, 1
    numbercounter = 0 #added this because there was no number counter for b. A was changing to b before b could change to a, they were getting each other confused
    total = 0
    while a <= limit:
        #if b % 2 == 0:   This line checks if the Fibonacci number is even, but we want the numbers to be odd
        if a % 2 == 1: #this line checks if the Fibonacci number is odd
            total = total + a #this should be adding to the total, not replacing the total with the new b value, also it should be added by a, not b, because a is the one going in order
            """numbercounter = a + b #this is preparing for b to be the next number in the fibonacci sequence
            a = b #this makes a equal to b
            b = numbercounter #this makes b the next number in the fibonacci sequence
            """

        a, b = b, a + b
       

    return total



# Add your test cases here
print(sum_even_fib(3)) #tester case, should print (0, 1, 1, 3)



# %%
 