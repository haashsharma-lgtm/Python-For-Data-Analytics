# Task 1 - List and append()

playlist_ids = [101, 102, 103, 104, 105]

playlist_ids.append(106)

print("Updated playlist IDs:", playlist_ids)



# Task 2 - List and extend()

cart_items = ['t-shirt', 'shoes']

cart_items.extend(['jeans', 'cap'])

print("Final cart items:", cart_items)



# Task 3 - pop()

def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item


order_list = ["Pizza", "Burger", "Biryani"]

removed = remove_last_item(order_list)

print("Removed item:", removed)
print("Updated order list:", order_list)



# Task 4 - Tuple and immutability

# insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")

# print(insta_filters)

# # Try to update the second filter
# insta_filters[1] = "Valencia"

# print(insta_filters)


#Task 5 - List vs Tuple

# Favorite genres can change, so we use a list
favorite_genres = ["Action", "Comedy", "Romance"]

# IRCTC train classes are fixed, so we use a tuple
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")

print("Favorite Genres:", favorite_genres)
print("Train Classes:", train_classes)