from datetime import date

def menu():
    try:
        menu = input("""To add balance only                  : B\n
To add expenditure only              : X\n
To check total net balance           : N\n
To check previous records            : R\n
To record both balance & expenditure : S\n
Enter: """)
        if menu.lower() in ['b', 'x', 'n', 'r', 's']:
            return menu.lower()
        else:
            raise ValueError("Invalid menu option. Please choose from B, X, N, R, or S.")
    except ValueError as e:
        print(e)
        return menu()

# Initialised Variables
Total = 0
Income = 0
Expense = 0
Date = date.today()
now = Date.strftime("%d-%m-%y")

def add_Income():                    # Income Function
    try:
        inp_sal = int(input("Add balance: "))
        if inp_sal < 0:
            raise ValueError("Income cannot be negative. Please try again.")
        return inp_sal
    except ValueError as e:
        print(e)
        return add_Income()

def add_Expense():                  # Expense Function
    try:
        inp_exp = int(input("Add expense: "))
        if inp_exp < 0:
            raise ValueError("Expense cannot be negative. Please try again.")
        return -inp_exp
    except ValueError as e:
        print(e)
        return add_Expense()

def total_income():                              # Returns total income
    try:
        Total_inc = 0
        with open("Income_rec.txt", "r") as file2R:
            for line in file2R:
                Total_inc += int(line.strip())
        return Total_inc
    except FileNotFoundError:
        print("No income records found.")
        return 0
    except ValueError:
        print("Error reading income records.")
        return 0

def total_expense():                    # Returns total Expense
    try:
        Total_Exp = 0
        with open("Expense_rec.txt", "r") as file3R:
            for line in file3R:
                Total_Exp += abs(int(line.strip()))
        return -Total_Exp
    except FileNotFoundError:
        print("No expense records found.")
        return 0
    except ValueError:
        print("Error reading expense records.")
        return 0

def net_balance():                # Returns total net balance
    income = total_income()
    expense = total_expense()
    net = income + expense
    print(f"Current total net balance: {net}")
    return net

def history():                                 # Loads history
    try:
        with open('MoneyRec.txt','r') as hist:
            record = hist.read()
        print(record)
    except FileNotFoundError:
        print("No history records found.")

def file_format():
    with open("MoneyRec.txt", "a") as rec:  # Appends Date
        rec.write(f"\n{now}--------------------------------------------------------")
    with open("MoneyRec.txt", "a") as file1:  # Opens the file and tracks our all record
        file1.write(f"\nIncome:{Income} | Expense:{Expense} | Net Balance:{Total}")

def record_to_file(file_name, value):
    """Helper function to record data to a file"""
    with open(file_name, "a") as file:
        file.write(f"{str(value)}\n")

# Basic Calculation and menu decision
match menu():
    case 'b':
        Income += add_Income()
        Total += Income + Expense
        file_format()
        record_to_file("Income_rec.txt", Income)
    case 'x':
        Expense += add_Expense()
        Total += Income + Expense
        file_format()
        record_to_file("Expense_rec.txt", Expense)
    case 'n':
        net_balance()
    case 'r':
        history()
    case 's':
        Income += add_Income()
        Expense += add_Expense()
        Total += Income + Expense
        file_format()
        record_to_file("Income_rec.txt", Income)
        record_to_file("Expense_rec.txt", Expense)
