
# Session 7: Conditional Statements
# Python Assignment

# Task 1: IPL Ticket Booking Eligibility
print("Task 1: IPL Ticket Booking")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for IPL ticket booking")
else:
    print("Not eligible")

print()


# Task 2: Influencer Classification
print("Task 2: Influencer Classification")

followers = int(input("Enter number of followers: "))

if followers < 10000:
    print("Micro Influencer")
elif followers <= 100000:
    print("Rising Star")
else:
    print("Celebrity")

print()


# Task 3: Zomato Free Delivery
print("Task 3: Zomato Free Delivery")

order_total = float(input("Enter your Zomato order total: "))

if order_total > 299:
    print("Apply Free Delivery")
elif order_total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")

print()


# Task 4: Flipkart Cashback
print("Task 4: Flipkart Cashback")

cart_value = float(input("Enter Flipkart cart value: "))
payment_method = input(
    "Enter payment method (UPI, Card, Cash): "
).strip().upper()

if cart_value > 1000:
    if payment_method == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")
