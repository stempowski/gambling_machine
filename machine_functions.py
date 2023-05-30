import keyboard 

MAX_LINES = 3 
def deposit():
    while(True):
        amount = input("how much you would like to deposit? PLN___")
        if amount.isdigit():
            amount = int(amount)
            if(amount) > 0:
                print("ok, you deposited: " + str(amount))
                break
            else:
                print("please deposit more than 0")
        else:
            print("please enter digit number")

    return amount

def get_number_of_lines():
    while(True):
        number_of_lines = ("enter number of lines between 1 and " + str(MAX_LINES))
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if(number_of_lines > 0):
                print("you entered: " + number_of_lines + " number of lines")
                break
            else:
                print("please enter positive number of lines! ")
    

def main():
    balance = deposit()

main()
