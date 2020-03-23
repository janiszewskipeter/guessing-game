import math  
import random 


def main():
    new_empty_list = [] 
    for i in range(10):
        new_empty_list.append(random.randint(1, 99))
    for i in range(10):
        user_guess = int(input("Enter an integer from 1 to 99: ")) 
        while new_empty_list[i] != user_guess: en with input user_guess do:
            if user_guess < new_empty_list[i]: 
                print("guess is low") 
                user_guess = int(input("Enter an integer from 1 to 99: ")) 
            elif user_guess > new_empty_list[i]: 
                print("guess is high") 
                user_guess = int(input("Enter an integer from 1 to 99: "))
            else: 
                break 
        print("you guessed it!") 

if __name__ == '__main__':
    main()