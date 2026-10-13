
# Session 8: Loops
# Python Assignment

# Task 1: Calculate Total Order Value
print("Task 1: Total Order Value")

order_amounts = [120, 250, 90, 310, 150]
total = 0

for amount in order_amounts:
    total += amount

print("Total Order Value:", total)
print()


# Task 2: Cricket Scores Using While Loop
print("Task 2: Cricket Scores")

scores = [45, 78, 102, 34, 67, 89]
i = 0

while i < len(scores):
    if scores[i] > 100:
        break

    print(scores[i])
    i += 1

print()


# Task 3: Flipkart Cart Using Continue
print("Task 3: Flipkart Cart")

item_prices = [299, 499, 199, 999, 149]
cart_total = 0

for price in item_prices:
    if price < 200:
        continue

    cart_total += price

print("Total Cart Value:", cart_total)
print()


# Task 4: Song Playlist Positions
print("Task 4: Song Playlist")

songs = [
    "Kesariya",
    "Believer",
    "Shape of You",
    "Blinding Lights",
    "Excuses"
]

for position, song in enumerate(songs, start=1):
    print(position, song)

print()


# Task 5: Instagram Followers Classification
print("Task 5: Instagram Followers")

followers_list = [120, 1500, 23000, 800, 45000]

for followers in followers_list:
    if followers < 1000:
        category = "Micro"
    elif followers <= 10000:
        category = "Influencer"
    else:
        category = "Celebrity"

    print(followers, "-", category)
