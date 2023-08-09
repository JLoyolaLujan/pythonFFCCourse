# print("hello"); 

# python is for everyone

#x = 6
#print(x)

#x = 43
#x = x + 1
#print(x); 

# speaking of conditionals

#x = 5; 
#if x < 10: 
#    print("smaller") 
#if x > 20: 
#    print("bigger")
#print("finis")

# speaking of repeated steps (loops)

#x = 5
#while x > 0 :
#    print(x)
#    x = x - 1
#print("blastoff!") 

# variables, expressions and statements

# constants are values that do not change; fixed values such as numbers, letters, strings are called constants because their value does not change
# numeric constants are as you expect --> print(123) --> 123
# string constants use single or double quotes --> print("hello") --> "hello"

# reserved words are words reserved for use (for, while, False, True)
# if you are to name variables DO NOT use reserved words

# a variable is a named place in the memory in which a programmer can store data 
# x = 12 --> you get to choose the name of the variable, you can even change its value (for that the name variable)

# variable naming rules: 
    # must start with a letter or _ 
    # must consist of letters, numbers and underscores
    # case sensitivity is a thing here as well as in javaScript!

# good: spam, egg, spam23, _spam
# bad: 23span, #egg, var.12
# different: spam, Spam, SPAM

# mnemonic variable names, that is to say, the name has to have "hints" about what the information will be for
# that, or, just don't be overly complicated (you can use x,y,z or a,b,c as valid variable names)

#hours = 32.00
#rate = 12.00
#pay = hours * rate
#print(pay)

# x = 2 --> assignment
# x = x + 2 ---> assignment with an expression
# print(x) ---> print statement
# the 2 is a constant

#x = 0.6 
#x = 3.9 * x * (1 - x)
#print(x) --> the value can be updated

# EXPRESSIONS

# numeric expressions, all the symbols for mathematical operations here are the same as in JS
# + addition, - substraction, * multiplication, / division, ** power, % reminder, etc
# it's not gonna be the SAME, I know, but so fat is quite similar

#little examples

#xx = 2 
#xx = xx + 2
#print(xx)

##yy = 440 * 12
##print(yy)
##zz = yy / 1000
##print(zz)

#jj = 23
#kk = jj % 5
#print(kk)

#print(4**3)

# understanding precedence here

#x = 1 + 2 * 3 - 4 / 5 ** 6
#print(x)
#is the same as
#y = 1 + (2 * 3) - (4 / (5 ** 6))
#print(y) 
#keep in mind, first the multiplication, then the power, then the division, and then the addition and the substraction

#some rules

#parentheses are always respected
#exponentiation (power)
#multiplication, division and reminder
#addition and substraction
#left to right <--- order

# TYPES OF DATA

#e = 2 + 4
#print(e) --> we are adding up to integers

#e = "hello " + "there"
#print(e) ---> we are concatenating two strings

# type matters in python, you can't concatenate an integer to a string with + like in JS

# to know the type you can use the type() function

#ee = "hello!"
#ff = 34 + 123 - 4
#print(type(ee)) --> class str
#print(type(ff)) --> class int

# numbers have two main types 
# integers are whole numbers (12, 23, -5)
# floating point numbers have decimal parts (2.04, 5.1)
# there are other number types which are variations on float and integers

#print(type(2))
#print(type(2.4))

# type conversions
# when you put an integer and a floating point in an expression together
# the integer is impicitly converted into a float

#x = 1 + 2.0
#print(type(x)) --> float
#print(x) 

# you can control this with the built in functions int() and float()

#x = 23
#print(type(x)) --> int
#f = float(x) --> turns into float
#print(type(f)) --> remains float
#print(type(x)) --> remains int

# continue at 1:14:44 from https://www.youtube.com/watch?v=8DvywoWv6fI&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=3&ab_channel=freeCodeCamp.org

# an integer division produces a floating point result

#x = 24 / 2
#print(x)
#print(type(x))

# remember, you can't concatenate a number to a string
# though, it the string solely has numbers, you can convert said string into a number with int() and float()

#stringus = "123" 
#numbus = int(stringus) 

#print(numbus)
#print(type(numbus))

# YOU CAN READ DATA FROM THE USER USING input() --> it returns a string

#nam = input("What's your name? ")
#print("welcome", nam)

# convert user input

#age = input("What's your age? ")
#info = int(age)
#print(type(info))
#print("your age is", info)

# from cel to fahr

#cel = input("enter current temperature in cel ")
#num = (int(cel) * 1.8) + 32
#print("the current temperature in fahr is", num)

# conditional statements

#x = int(input("enter a number:"))
#if x < 10:
#    print("smaller than 10")
#if x > 10: 
#    print("bigger than 10")
# print(2 > 1) --> returns a boolean

# the conditional operators are >, <, >=, <= != and == ... remember that the = is used for assignment!

# you can put the condition and the body in the same line

#x = 23
#if x > 10: print("number is bigger")

# as long as the line is indented, you still are in the same if

#x = 12

#if x > 10: ---> if I change the > for a < then all the code indented below does not execute
#    print("bigger")
#    print("the number is still bigger")
#    print("hello there, this is still indented so, hi")

# INDENTATION

# use indent after an if statement or for statement (after :)

# mantain indent to indicate the scope of the block (which lines are affected by the if/for)

# reduce indent back to the level of the if statement or for statement to indicate the end of the block

# blank lines are ignored - they do not affect indentation

# comments on a line by themselves are ignored with regard to indentation

# be careful using the TAB key; python is very sensitive when it comes to indentation

# use spaced instead (on TAB is equal to 3 spaces)

#x = int(input("enter a number:"))
#if(x > 2) : 
#    print("bigger than 2")
#    print("still bigger")
#print("out of the range if the if statement above")

# ---> start of for
#for i in range(5) :
#    print(i)
    # ---> start of if
#    if i > 2 : 
#        print("bigger than 2")
    # ---> end of if
#    print("all done with i", i) 
# ---> end of for
#print("all done")

#num = int(input("enter a number:"))

#if num > 1 : 
#    print("number is bigger than 1")
#    if num < 100 : 
#        print("number is lesser than 100")
#print("all done")

# two way decision (if... or else)

#num = int(input("enter a number:"))
#if num > 2 : 
#    print("bigger than 2")
#else : 
#    print("smaller than 2")
#print("all done")

# multi-way (if, elif and else)

#num = int(input("enter a number:"))
#if num < 2 : 
#    print("number is smaller than 2")
#elif num == 2 : 
#    print("number is 2")
#else : 
#    print("number is bigger than two")
#print("all done")

# you can have no else and multiple elifs

#num = int(input("enter a number: "))
#if num < 2 : 
#    print("number is lesser than 2")
#elif num == 2 : 
#    print("number is 2")
#elif num > 2 : 
#    print("number is bigger than 2")
#print("all done")

# the order of your question matter

#num = int(input("enter a number: "))

#if num < 2 : 
#    print("lesser than 2")
#elif num < 10 :
#    print("lesser than 10")
#elif num < 20 : 
#    print("lesser than 20")
#print("all done")

# some user inputs might make the program explode, that's why we have the try - except in python

# surround a dangerous section of code with try and except
# if the code in the try works - the except is skipped
# if the code in the try fails - it jumps to the except section

#astr = "hello"

#try: 
#    istr = int(astr) # --> will blow up
#except: 
#    istr = -1 # --> so it jumps right over there
#print("first", istr)

#astr = "123"
#try: 
#    istr = int(astr) # --> will work
#except: 
#    istr = -1 # --> will be ignored
#print("second", istr) 

# remember that the try section, if it is bound to explode, all of its content is ignored
# so do not put there important chunks of code that you want to run

# a simple real life example

#rawstr = input("enter a number:")
#try: 
#    ival = int(rawstr)
#except: 
#    ival = -1
# ---> whatever the result, the code continues
#if ival > 0 : 
#    print("nice work")
#else : 
#    print("not a number")

# functions (we don't want to repeat ourselves)

#def thing(name) : 
#    print("hi", name)
#    print("how are you?") function ends at de-indentation

#x = input("enter your name")
#thing(x) runs because of this function call

# we have built-in functions (int(), type() input(), etc...)
# and functions made by ourselves 

# again, we avoid naming variables or functions with reserved names

# the function is a reusable piece of code that takes arguments as input
# we define a function using the "def" reserved word
# we call/invoke the function by using the functio name, parentheses and arguments in an expression

# two built in functions to analyze 

#a = max("hello where")
#b = min("hello there")

# max will search for the "biggest" character in given strings, whilst 
# min will search for the "smallest" character

# each character will be assigned to its respective variable through = 
# because each function is returning such values

#print(a) # returns w
#print(b) # returns " "

#str = "123"
#num = int(str)
#print(type(num))

# functions of our own

#def print_lyrics() : --> (once the function is defined we are able to call it later)
#    print("heartaches by the number")
#    print("troubles by the score")
#print_lyrics() --> (here is the call)

# working with arguments 

#def celToFahr(value) : 
#    return (value * 1.8) + 32
#print(celToFahr(32))

#def language(lang) : --> here the "lang" is a parameter, a space to which we pass an argument when we invoke the function
#    if lang == "es" : 
#        return "español"
#    elif lang == "en" : 
#        return "english"
#    elif lang == "guar" : 
#        return "guaraní"
#    else : 
#        return "no language has been selected"
#print(language("guar"))

# remember that the return statement ends the function, just like in JS
    
# Multiple parameters and arguments

#def sum(a,b) : 
#    added = a + b
#    return added
#print(sum(1,2))

# non fruitful functions (or void functions) are those that don't return a value

# loops and iterations

#n = 5
#while n > 0 : 
#    print(n)
#    n = n - 1
#print("blastoff!!")
#print(n)

#n = 5
#while n > 0 : 
#    print("hello!")
#    n = n - 1 <--- without this we would have created an infinite loop

# we'll refer to the n above as the "iteration variable"
# which will garantee us that the loop works as it should

# though we can control the loop with other statements, such as "break"
# it quite literaly is the same "break" as in JavaScript

#while True : 
#    line = input("> ") ---> this little arrow is way too cool, imma use it a LOT
#    if line == "done" : 
#        break # <-- loop shoult end here if the if statement is satisfied
#    print(line)
#print("all done!")

# the "break" statements ends the whole loop
# we can use the "continue" if we want to skip an iteration

#while True : 
#    line = input("> ")
#    if line[0] == "#" : 
#        continue ---> if first character of string is # don't print
#    if line == "done" : 
#        break
#    print(line)
#print("all done")

#while True : 
#    print("enter a number")
#    line = input("> ")
#    if line == "stop" : break
#    elif int(line) % 2 == 0 :
#        print("even")
#    elif int(line) % 2 != 0 :
#        print("odd")
#print("done")

# break and continue give us control over the infinite loops created with "while True : "
# these kinds of loops, those that continue iterating until a logical condition becomes False,
# are called "indefinite loops"

# definite loops! 

# while indefinite loops use the while keyword, definite loops use the "for" keyword
# we use the for when we want to iterate over a list of items (just like in JS)
# with the for construct, we can write a loop to run once for each of the items in a set

# these loops are "definite" because they execute an exact number of times 
# we say that "definite loops iterate through the members of a set"

# a simple example 

#for i in [5,4,3,2,1] : 
#    print(i)
#print("blastoff!!")

#n = [1,2,3,4,5]

#for i in n : 
#    print(i, n)

# the i is like an assignment that will take succesive values
# first it'll be 1, then 2, then 3, and so on and so forth

#names = ["jimmy", "jeremy", "johnnathan", "Grumblo"]

#for i in names : 
#    print(i, names)

# the iteration variable (i) moves through all the values in the sequence
# the loop body (print(i, names)) is executed for each value in the sequence

# loop idioms: what we do in loops
# loop idioms are patters that have to do with how we construct loops

#largest = -1
#print("before", largest)
#for num in [9,41,12,3,74,15] : 
#    if num > largest : 
#        largest = num
#    print(largest, num)
#print("after", largest)

# more patters we can use in a loop

# counting variable (how many times we execute a loop)

#num = 0 
#group = [9,41,12,3,74,15]
#print("before", num)
#for i in group : 
#    num = num + 1
#    print(num, i)
#print("after", num)

# summing in a loop

#num = 0 
#group = [9,41,12,3,74,15]
#print("before", num)
#for i in group : 
#    num = num + i
#    print(num, i)
#print("after", num) # the result is the total addition of the numbers inside the list "group"

# now we can get the average

#num = 0 
#sum = 0
#group = [9,41,12,3,74,15]
#print("before", num)
#for i in group : 
#    num = num + 1
#    sum = sum + i
#    print(num, sum, i)
#print("the average is:", (sum / num))

# filtering a loop

#group = [9,41,12,3,74,15]
#print("before")
#for i in group : 
#    if i > 20 :
#        print(i)
#print("after")

# filter using a boolean

#found = False
#num = 0
#group = [9,41,12,3,74,15]
#print("before", num, found)
#for i in group : 
#    if i == 3 :
#        found = True
#        num = 3
#        break
#print("after", num, found)

# find the smallest

#largest = -1
#print("before", largest)
#for num in [9,41,12,3,74,15] : 
#    if num > largest : 
#        largest = num
#    print(largest, num)
#print("after", largest)

#smallest = largest
#print("before", smallest)
#for num in [9,41,12,3,74,15] : 
#    if num < smallest : 
#        smallest = num
#    print(smallest, num)
#print("after", smallest)

# solition 2
# we will take the hypothesis that maybe the first number is the smallest
# if it is, then the first will be returned, else it'll be replaced accordingly
# as the loop runs

# the same we can do when looking for the largest number

#group = [9,41,12,3,74,15]
#smallest = group[0]
#print("before", smallest)
#for num in group : 
#    if num < smallest : 
#        smallest = num
#    print(smallest, num)
#print("after", smallest)

# the solution from the Course introduces the None type which, as far as I understand
# is similar to the "undefined" from JavaScript

#smallest = None
#print("before", smallest)
#for i in [9,41,12,3,74,15] : 
#    if smallest == None : 
#        smallest = i
#    if i < smallest : 
#        smallest = i
#    print(smallest, i)
#print("after", smallest)

# now the largest with the same method

#largest = None 
#print("before", largest)
#for i in [9,41,12,3,74,15] : 
#    if largest == None : --> I can write it as "if largest is None" and would work exactly the same
#        largest = i
#    if i > largest : 
#        largest = i
#    print(largest, i)
#print("after", largest)

# adding up the logical operators "is" and "is not" to the mix
# they are similar to "==" and "!=" respectively, but far stronger

#group = [45,324,7,34,1,45,9] 
#smallest = None
#print("before", smallest)
#for i in group : 
#    if smallest is None : 
#        smallest = i
#    if i < smallest : 
#        smallest = i 
#    print(smallest, i)
#print("after", smallest)

# why are the "is" and "is not" far stronger? 
# if I ask something like "0 == 0.0" I'm asking if the 
# int 0 is equal to the float 0.0
# with the == operator the expression will return True
# but if I ask "0 is 0.0", the expression will return False

# the value AND type have to be the same for the expression to return True
# sort of like === in JS 

# no conversion is done with the "is" and "is not"
# the teacher tends to use the "is" and "is not" in booleans and None types
# while trying to use the "==" on strings, floats and ints

# just in case ---> Chapter 6: strings at 2:58:49