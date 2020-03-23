# program gives a random number to guess by the user, if guess is lower or higher than the number
# program shows a message 
import math # import match module   
import random # import random module

def main():
    a = [] #initialize empty list
    a.append(random.randint(1, 99))# adds 1st random number to [a] list
    a.append(random.randint(1, 99))# adds 2nd random number to [a] list
    a.append(random.randint(1, 99))# adds 3th random number to [a] list
    a.append(random.randint(1, 99))# adds 4th random number to [a] list
    a.append(random.randint(1, 99))# adds 5th random number to [a] list
    a.append(random.randint(1, 99))# adds 6th random number to [a] list
    a.append(random.randint(1, 99))# adds 7th random number to [a] list
    a.append(random.randint(1, 99))# adds 8th random number to [a] list
    a.append(random.randint(1, 99))# adds 9th random number to [a] list
    a.append(random.randint(1, 99))# adds 10th random number to [a] list
    for i in range(10): # loop for i in range 1 -10
        g = int(input("Enter an integer from 1 to 99: ")) # takes an integer input and creates a variable g
        while a[i] != g: # while firs number of a list is not even with input g do:
            if g < a[i]: # if user input lover than first index of the list 
                print("guess is low") # print text
                g = int(input("Enter an integer from 1 to 99: "))# takes an integer input and creates a variable g
            elif g > a[i]: #else if user input higher than first etc element of the list
                print("guess is high") #print text
                g = int(input("Enter an integer from 1 to 99: "))# takes an integer input and creates a variable g
            else: # any other input will:
                break #end loop 
        print("you guessed it!") #print text

    b = [] #initialize empty list
    b.append(random.randint(1, 49))# adds 1st random number to [b] list
    b.append(random.randint(1, 49))# adds 2nd random number to [b] list
    b.append(random.randint(1, 49))# adds 3th random number to [b] list
    b.append(random.randint(1, 49))# adds 4th random number to [b] list
    b.append(random.randint(1, 49))# adds 5th random number to [b] list
    b.append(random.randint(1, 49))# adds 6th random number to [b] list
    b.append(random.randint(1, 49))# adds 7th random number to [b] list
    b.append(random.randint(1, 49))# adds 8th random number to [b] list
    b.append(random.randint(1, 49))# adds 9th random number to [b] list
    b.append(random.randint(1, 49))# adds 10th random number to [b] list
    for i in range(10):# loop for i in range 1 -10
        g = int(input("Enter an integer from 1 to 49: ")) # takes an integer input and creates a variable g
        while b[i] != g:# while firs number of a list is not even with input g do:
            if g < b[i]:# if user input lover than first index of the list 
                print("guess is low")#print text
                g = int(input("Enter an integer from 1 to 49: "))# takes an integer input and creates a variable g
            elif g > b[i]:#else if user input higher than first etc element of the list
                print("guess is high")#print text
                g = int(input("Enter an integer from 1 to 49: "))# takes an integer input and creates a variable g
            else: # other way than if or elif
                break#end loop 
        print("you guessed it!")#print text
if __name__ == '__main__':
    main()