# Task 1 - Variables and Data Types

followers = 5000
average_rating = 4.5
favorite_app = "Instagram"
is_premium_user = True

print(followers, type(followers))
print(average_rating, type(average_rating))
print(favorite_app, type(favorite_app))
print(is_premium_user, type(is_premium_user))


# Task 2 - Zomato Order with 18% GST

price = input("Enter your Zomato order price: ")

price = float(price)

gst = price * 18 / 100

final_bill = price + gst

print("Final bill amount:", final_bill)


# Task 3 - Flipkart Cart Value

prices = ['199.99', '299.50', '150']

float_prices = [float(price) for price in prices]

total_cart_value = sum(float_prices)

print("Float prices:", float_prices)
print("Total cart value:", total_cart_value)



# Task 4 - Discount Applicable

def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False


print(is_discount_applicable(450))
print(is_discount_applicable(750))


# Task 5 - Spotify Ratings

ratings = ['4.5', '3.0', '5', '4.2']

float_ratings = [float(rating) for rating in ratings]

highest_rating = max(float_ratings)

print("Float ratings:", float_ratings)
print("Highest rating:", highest_rating)