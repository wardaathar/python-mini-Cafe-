menu = {
  'Biryani': 100,
  'Chatt': 180,
  'Qourma': 200,
  'Nihari': 400,
}

print("Welcome to Python Restaurant")
print("Biryani: 100\nChatt: 180\nQourma: 200\nNihari: 400")

Order_total = 0

def add_item():
    item = input("Enter your item: ")
    if item in menu:
        global Order_total
        Order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available. Please choose another item.")
        add_item()

# First item
add_item()
# Ask if customer wants to add more
while True:
    more = input("Would you like to add another item? (Yes/No): ").strip().lower()
    if more == 'yes':
        add_item()
    elif more == 'no':
        break
    else:
        print("Please enter 'Yes' or 'No'.")

print(f"Total amount to pay is {Order_total}")