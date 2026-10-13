
# Session 5: Lists and Tuples
# Python Assignment

# Task 1: Spotify Playlist IDs
print("Task 1: Spotify Playlist IDs")

playlist_ids = [101, 102, 103, 104, 105]
playlist_ids.append(106)

print("Updated Playlist IDs:", playlist_ids)
print()


# Task 2: Flipkart Shopping Cart
print("Task 2: Flipkart Shopping Cart")

cart_items = ["t-shirt", "shoes"]
cart_items.extend(["jeans", "cap"])

print("Final Cart Items:", cart_items)
print()


# Task 3: Remove Last Zomato Order
print("Task 3: Zomato Order List")

def remove_last_item(order_list):
    return order_list.pop()

orders = ["Pizza", "Burger", "Pasta"]

removed_item = remove_last_item(orders)

print("Removed Item:", removed_item)
print("Updated Order List:", orders)
print()


# Task 4: Instagram Filters Tuple
print("Task 4: Instagram Filters")

insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")

print("Original Filters:", insta_filters)

try:
    insta_filters[1] = "Valencia"
except TypeError as error:
    print("Error:", error)

# Tuples are immutable, so their items cannot be
# changed using direct assignment.
print()


# Task 5: Choosing List vs Tuple
print("Task 5: List vs Tuple")

# Use a list because favorite genres may change.
favorite_genres = ["Comedy", "Action", "Drama"]
favorite_genres.append("Thriller")

print("Favorite Genres:", favorite_genres)

# Use a tuple for this fixed collection of train classes.
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")

print("Train Classes:", train_classes)
