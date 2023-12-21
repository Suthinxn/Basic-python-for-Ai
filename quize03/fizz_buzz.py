
def fizz_buzz_game():
    print("Welcome to FizzBuzz Game")
    num_fizz = 0
    num_fizzbuzz = ""
    num_sum =0
    while True:

        number_input = int(input("Enter number: "))
        if (number_input % 3 == 0 or number_input % 3 == -0) and (number_input % 5 == 0 or number_input % 5 == -0 ):
            num_fizzbuzz += "FizzBuzz"
            num_sum += number_input %  len(num_fizzbuzz) 

        elif (number_input % 5 == 0 or number_input % 5 == -0):
            num_fizzbuzz += "Buzz"


        elif (number_input % 3 == 0 or number_input % 3 == -0):
            num_fizzbuzz += "Fuzz"
            num_sum += number_input %  len(num_fizzbuzz) 


        else: 
            num_fizzbuzz += "NoFizzBuzz" 
            num_sum += number_input %  len(num_fizzbuzz) 

        

        if num_sum > 20:
            break

    last_num = num_sum % number_input
    print(f"Your score:{last_num} ")

if __name__  == '__main__':
    
    fizz_buzz_game()