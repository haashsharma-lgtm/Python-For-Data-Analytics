
# Session 6: Dictionaries and Sets


# Task 1: Create a Playlist Price Dictionary
print("Task 1: Playlist Prices")

playlist_prices = {
    "Chill Hits": 100,
    "Pop Mix": 150,
    "Workout Beats": 200,
    "Daily Mix": 120,
    "Party Hits": 180
}

print("Original Playlist Prices:", playlist_prices)
print()


# Task 2: Update a Playlist Price
print("Task 2: Update Playlist Price")

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Chill Hits", 250)

print("Updated Playlist Prices:", playlist_prices)
print()


# Task 3: Delete a Playlist
print("Task 3: Delete a Playlist")

del playlist_prices["Party Hits"]

print("Playlist Prices After Deletion:", playlist_prices)
print()


# Task 4: Set Union and Intersection
print("Task 4: Restaurant Sets")

# Restaurants ordered from Zomato
set1 = {"Dominos", "Subway", "La Pinoz", "Burger King"}

# Restaurants ordered from Swiggy
set2 = {"Subway", "McDonalds", "Dominos", "Pizza Hut"}

union_result = set1.union(set2)
intersection_result = set1.intersection(set2)

print("Union:", union_result)
print("Intersection:", intersection_result)
