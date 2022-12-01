import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

sympol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, sympols):
    all_sympols = []
    for sympol, sympol_count in sympols.items():       #items in dictionary = key + value
        for _ in range(sympol_count):
            all_sympols.append(sympol)
    columns = []
    for _ in range(cols):
        column = []
        current_sympols = all_sympols[:]                #make a copy of all_sympols
        for _ in range(rows):
            value = random.choice(current_sympols)
            current_sympols.remove(value)
            column.append(value)                        #add value to column
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()
                
        
def deposit():
    while True:
        amount = input("What do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a number ")
    return amount

def get_bet():
    while True:
        amount = input("What do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Please enter a number ")
    return amount
def get_numbet_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter a number ")
    return lines



def main():
    balance = deposit()
    lines = get_numbet_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount, your current balance is: ${balance}")
        else:
            break
            
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    #print(balance, lines)

main()

slots = get_slot_machine_spin(ROWS, COLS, sympol_count)
print_slot_machine(slots)