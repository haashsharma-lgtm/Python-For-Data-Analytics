
# Session 9: Functions
# Python Assignment

# Task 1: Calculate Final Price
print("Task 1: Calculate Final Price")

def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate)
    return final_price

result = calculate_final_price(1200, 0.15)
print("Final Price:", result)
print()


# Task 2: Calculate Delivery Charge
print("Task 2: Delivery Charge")

def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 30
    else:
        return 50

print("Ahmedabad Charge:", get_delivery_charge(500))
print("Surat Charge:", get_delivery_charge(500, "Surat"))
print()


# Task 3: Format Coupon Message
print("Task 3: Coupon Message")

def format_coupon_message(username, discount=10):
    return f"Hi {username}, you get {discount}% off!"

print(format_coupon_message("Rahul", 20))
print(format_coupon_message("Amit"))
print()


# Task 4: Apply Discount with Default Rate
print("Task 4: Apply Discount")

def apply_discount(price, rate=0.10):
    return price - (price * rate)

result = apply_discount(1000)
print("Final Price:", result)
print()


# Task 5: Calculate Cashback
print("Task 5: Calculate Cashback")

def calculate_cashback(amount, cashback_rate=0.05):
    return amount * cashback_rate

zomato_cashback = calculate_cashback(500)
flipkart_cashback = calculate_cashback(2000, 0.07)

print("Zomato Cashback:", zomato_cashback)
print("Flipkart Cashback:", flipkart_cashback)
