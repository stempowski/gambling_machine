import keyboard 
import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns =[]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


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
        number_of_lines = input("enter number of lines between 1 and " + str(MAX_LINES))
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if(number_of_lines > 0 and number_of_lines <= MAX_LINES):
                print("you entered: " + str(number_of_lines) + " number of lines")
                break
            else:
                print("please enter positive number of lines higher than 0 and lower than - " + str(MAX_LINES))
        else:
            print("pls enter a digit")
    return number_of_lines

def get_bet():
    while(True):
        bet = input("What would you like to bet?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET < bet < MAX_BET:
                break
            else:
                print(f"amount must be in between: ${MIN_BET} - ${MAX_BET})")
        else:
            print("please enter a number") 
    return bet

def main(): 
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough balance on your account")
        else:
            break
    print(f"you are betting {bet} on {lines}. Total bet is equal to: {total_bet}")
    #print(str(balance) + "\N"+ str(lines) + "\N"+ str(bet))
    print(f"Details: \nbalance: {balance}\nlines: {lines}\n{bet}")
main()
