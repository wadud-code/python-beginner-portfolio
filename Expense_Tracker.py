
print("="*80)
print("Welcome to matriceDB the Expense Tracker!")
print("="*80)
Expense = {}

def add_expense():
    total_expence = sum(Expense.values())
    if total_expence > 100:
        print("====WARNING====")
        print("You are spendig extravagantly")
        choice = input("Do you want to continue(y/n): ").lower()
        if choice!="y":
            print("Expense Addition Cancelled")
            return
        
    try:
        
               item_name = input("Enter the name of the item:  ")
               price = float(input("Enter the price of the item:  "))
               Expense[item_name] = price
        
               print("Expense Entered Sucessfully")
        
    except ValueError:
                print("Invalid Input, try entering valid values once again")
        
             


def see_expense():

    for item_name,price in Expense.items():
      print(f"{item_name} price is {price}")

def check_statistics():
    print("Expense Statistic")
    prices = list(Expense.values())
    if not prices:
        print("No price yet")
    else:

      mini = min(prices)
      maxi = max(prices)
      average = sum(prices)/len(prices)
      print(f"{mini}\n{maxi}\n{average}")
def manu():
    print("1:Add Expense")
    print("2:See Expense")
    print("3:Check Statistic")
    option = int(input("Enter:1,2,3:  "))
    if (option==1):
        add_expense()
    elif (option==2):
        see_expense()
    elif option==3:
         check_statistics()
    else:
        print("Invalid Input")
while True:
    manu()


