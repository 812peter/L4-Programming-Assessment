import random as rnd
import time
import csv
from datetime import datetime

# define items in the vending machine
item1 = {"name": "Water", "price": 1.00, "stock": 10}
item2 = {"name": "Soda", "price": 1.20, "stock": 8}
item3 = {"name": "Energy Drink", "price": 2.00, "stock": 5}
item4 = {"name": "Cookie", "price": 0.50, "stock": 2}
item5 = {"name": "Crisps", "price": 1.50, "stock": 0}

menu = [item1, item2, item3, item4, item5]


# initialise global variables
order_num = rnd.randint(100, 1000)
allowed_coins = [0.20, 0.50, 1.00, 2.00]
balance = 0.00
items_bought = []
total_spent = 0.00
true_total = 0.00
change_given = []
total_money_added = 0.00
filename = ""

def reset_vars():
    """
    resets all global variables between customers to prepare for a new order
    """
    global order_num, balance, items_bought, total_spent, true_total, change_given, total_money_added

    order_num += 1
    balance = 0.00
    items_bought = []
    total_spent = 0.00
    true_total = 0.00
    change_given = []
    total_money_added = 0.00

def check_input_coin(input):
    """
    validates and processes a coin inserted by the user
    """
    global balance, total_money_added

    try:
        if float(input) in allowed_coins:
            balance += float(input)
            total_money_added += float(input)
            return True
    except ValueError:  # handles non-numeric inputs
        return False

def insert_coins():
    """
    allows the user to insert coins until they type 'done'
    """
    while True:
        print(); print(f"Current balance: £{balance:.2f}")
        input_coin = input(f"Insert a coin ({', '.join([f'£{coin:.2f}' for coin in sorted(allowed_coins)])}) or type 'done' to finish: ")

        if input_coin.lower() == "done":
            break
        elif not check_input_coin(input_coin):
            print(); print("Error: invalid input.")

def print_menu():
    """
    displays the vending machine menu
    """
    print(); print("-------- Vending Machine Menu --------"); print()

    i = 1
    for item in menu:
        print(f"{i}. {item['name']} - £{item['price']:.2f}   ({item['stock']} in stock)")
        i += 1

    print(); print("--------------------------------------")

def check_input_purchase(input):
    """
    checks if the user input matches any item name in the menu
    """
    for item in menu:
        if input.lower() == item["name"].lower():
            return True
    return False

def create_receipt():
    """
    creates a CSV receipt for the transaction with purchase details
    """
    global filename
    filename = f"receipt_{order_num}.csv"
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # header: order number and timestamp
        writer.writerow([f"ORDER NUMBER: #{order_num}"])
        writer.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
        writer.writerow(["Count", "Item", "Price (£)", "Discount", "Final Price (£)"])

        # write each purchased item to the file
        count = 1
        for item in items_bought:
            writer.writerow([
                count,
                item["name"],
                f"{item['price']:.2f}",
                f"{item['discount']:.0f}%",
                f"{(item['price'] * (1 - item['discount']/100)):.2f}"
            ])
            count += 1
        
        # summary: totals and change
        writer.writerow([])
        writer.writerow(["", "TOTAL SPENT", "", "", f"£{total_spent:.2f}"])
        writer.writerow(["", "MONEY ADDED", "", "", f"£{total_money_added:.2f}"])
        writer.writerow(["", "CHANGE GIVEN", "", "", f"£{sum(change_given):.2f}"])
        file.close()
        
    print(); print(f"Receipt created for order #{order_num}.")

def finish():
    """
    handles change dispensing
    """
    global change_given, balance, allowed_coins

    # sort coins from largest to smallest to give the fewest coins possible
    allowed_coins.sort(reverse=True)

    for coin in allowed_coins:
        while balance >= coin - 0.001:  # for floating-point rounding errors
            change_given.append(coin)
            balance -= coin

    # bonus feature
    bonus = False
    if order_num % 2 == 1 and total_spent > 2:
        bonus = True
        change_given.append(1.0)

    # print coins being dispensed one by one
    if change_given:
        print(); print("Dispensing change:", flush=True)
        for coin in change_given:
            time.sleep(1)
            print(f"£{coin:.2f}", flush=True)
        if bonus:
            time.sleep(1)
            print(); print(f"[Bonus change of £1.00 due to odd-numbered order (#{order_num}) and spending over £2.00]")
    else:
        print(); print("No change to dispense.")
    
    create_receipt()
    print(); print("Thank you for the purchase! Have a great day!")

def check_discount(current_total=None, current_items=None):
    """
    calculates the discount rate based on total spent and number of items
    """
    # use current totals if provided, otherwise use global totals
    total = current_total if current_total is not None else total_spent
    items = current_items if current_items is not None else items_bought

    if total > 7.0:
        return 0.85  # 15% discount
    elif total > 5.0:
        return 0.9   # 10% discount
    elif len(items) >= 3:
        return 0.95  # 5% discount
    else:
        return 1.0   # no discount

def purchasing():
    """
    handles the process of selecting and buying items
    """
    global balance, total_spent, items_bought, menu, true_total

    while True:
        print_menu()
        print(); print(f"Current balance: £{balance:.2f}")
        user_input = input("Select an item by name, or type 'add' to top up your balance, or type 'exit' to quit: ")

        if user_input.lower() == "exit":
            finish()
            break
        
        elif user_input.lower() == "add":
            insert_coins()

        else:
            if check_input_purchase(user_input):
                # find the item object matching the user input
                for item in menu:
                    if item["name"].lower() == user_input.lower():
                        current_item = item

                if current_item["price"] > balance:
                    print(); print("Error: insufficient balance.")

                elif current_item["stock"] == 0:
                    print(); print("Sorry, we are out of stock. Choose another item.")

                else:
                    """
                    discount recalculated including current purchase;
                    eg, third item bought has 5% discount, it doesn't just apply for the forth purchase; 
                    eg, cookie = £0.50, total spent = £4.85, so 10% discount is triggered for the cookie too
                    """
                    temp_items_bought = items_bought + [current_item]
                    temp_true_total = true_total + current_item["price"]

                    discount = check_discount(temp_true_total, temp_items_bought)
                    spent_now = current_item["price"] * discount

                    # store discount percentage in item dictionary
                    current_item["discount"] = round(100 * (1 - discount))

                    # update balances and totals
                    balance -= spent_now
                    true_total += current_item["price"]
                    total_spent += spent_now
                    items_bought.append(current_item.copy())  # store a copy to prevent mutation
                    current_item["stock"] -= 1  # Reduce stock

                    # simulate dispensing animation
                    print()
                    print("Dispensing item.", end="", flush=True)
                    time.sleep(1); print(".", end="", flush=True); time.sleep(1); print(".", flush=True); time.sleep(1); print()
                    print(f"Purchased {current_item['name']} for £{spent_now:.2f} (discount: {round(100 * (1 - discount))}%)")
                    print(f"Total spent: £{total_spent:.2f}")

            else:
                print(); print("Error: invalid input.")

def main():
    """
    main program loop that serves multiple customers continuously
    """
    while True:
        insert_coins()
        purchasing()
        reset_vars()
        print(); print("Next customer...")

if __name__ == "__main__":
    main()