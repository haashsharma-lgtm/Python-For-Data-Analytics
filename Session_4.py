# Task 1 - String upper() and lower()

var="Redmi Note 12 Pro"
print(var.upper())
print(var.lower())

# Task 2 - Clean Brand Name

def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name


result = clean_brand_name(" oneplus-Nord ")

print(result)


# Task 3 - Split and Slicing

product = "Apple iPhone 14 Pro Max"

words = product.split()

brand = words[0]
model = " ".join(words[1:])

print("Brand:", brand)
print("Model:", model)


# Task 4 - Format Product Display

def demo(name,price):
    return f"prodct{name}-${price}"

print(demo("Redmi Note 12 Pro", 19999))


# Task 5 - Clean Product Names

# Task 5 - Clean Product Names

products = [' mi-Band 5 ', 'SAMSUNG-Galaxy', 'realme-Book']

cleaned_products = []

for product in products:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()
    
    cleaned_products.append(product)

print("Cleaned products:", cleaned_products)