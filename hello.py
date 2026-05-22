# Duka Smart Billing Program

# Part 1 — Welcome & customer info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"\nWelcome to Duka Smart, {name}! (Age: {age})\n")

# Part 2 — Collect 3 items
items = []
for i in range(1, 4):
    print(f"Enter details for item {i}:")
    item_name = input("Item name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit (KES): "))
    line_total = quantity * price
    items.append({"name": item_name, "quantity": quantity, "price": price, "line_total": line_total})
    print()

# Part 3 — Calculate totals
subtotal = sum(item["line_total"] for item in items)
vat = subtotal * 0.16
grand_total = subtotal + vat

# Print formatted receipt
print("\n--- RECEIPT ---\n")
for idx, item in enumerate(items, start=1):
    print(f"{idx}. {item['name']:<15} x{item['quantity']}  =  KES {item['line_total']:.2f}")
print()
print(f"Subtotal  :  KES {subtotal:.2f}")
print(f"VAT (16%) :  KES {vat:.2f}")
print(f"TOTAL     :  KES {grand_total:.2f}")

# Part 4 — Change calculator
cash = float(input("\nCash paid (KES): "))
if cash >= grand_total:
    change = cash - grand_total
    print(f"Change    :  KES {change:.2f}")
else:
    shortfall = grand_total - cash
    print(f"Shortfall :  KES {shortfall:.2f} (Insufficient cash!)")
# Duka Smart Billing Program

