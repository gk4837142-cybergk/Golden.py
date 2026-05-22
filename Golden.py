#!usr/bin/env python3
# assigning the resturant name
print("\n--- GOLDEN TULIP RESTAURANT ---\n")
client_name = input("Enter your name: ")
print(f"Welcome {client_name} to Golden tulip restaurant")

print("\n--- MENU ---\n")
# Professional Menu System

# Define menu as a list of dictionaries
menu = [
    {"name": "Pizza", "price": 800, "quantity": 1},
    {"name": "Burger", "price": 500, "quantity": 1},
    {"name": "Chapati", "price": 30, "quantity": 1},
    {"name": "Ugali", "price": 50, "quantity": 1},
    {"name": "Nyama Choma", "price": 1200, "quantity": 1},
]

# Print menu in a neat format
print("========== Duka Smart Menu ==========")
print(f"{'Item':<15}{'Price (KES)':<15}{'Quantity Available':<20}")
print("-" * 50)

for item in menu:
    print(f"{item['name']:<15}{item['price']:<15}{item['quantity']:<20}")

print("=====================================")

foods = []
for i in range(1, 5):
    print(f"Enter the type of food you want to order {i}:")
    item_name = input("food name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit (KES): "))
    line_total = quantity * price
    foods.append({"name": item_name, "quantity": quantity, "price": price, "line_total": line_total})
    print()