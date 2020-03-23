# program gives new_empty_list random number to guess by the user, if guess is lower or higher than the number
# program shows new_empty_list message 
import math # import match module   
import random # import random module

def main():
    new_empty_list = [] #initialize empty list
    new_empty_list.append(random.randint(1, 99))# adds 1st random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 2nd random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 3th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 4th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 5th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 6th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 7th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 8th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 9th random number to [new_empty_list] list
    new_empty_list.append(random.randint(1, 99))# adds 10th random number to [new_empty_list] list
    for i in range(10): # loop for i in range 1 -10
        user_guess = int(input("Enter an integer from 1 to 99: ")) # takes an integer input and creates new_empty_list variable user_guess
        while new_empty_list[i] != user_guess: # while firs number of new_empty_list list is not even with input user_guess do:
            if user_guess < new_empty_list[i]: # if user input lover than first index of the list 
                print("guess is low") # print text
                user_guess = int(input("Enter an integer from 1 to 99: "))# takes an integer input and creates new_empty_list variable user_guess
            elif user_guess > new_empty_list[i]: #else if user input higher than first etc element of the list
                print("guess is high") #print text
                user_guess = int(input("Enter an integer from 1 to 99: "))# takes an integer input and creates new_empty_list variable user_guess
            else: # any other input will:
                break #end loop 
        print("you guessed it!") #print text

if __name__ == '__main__':
    main()