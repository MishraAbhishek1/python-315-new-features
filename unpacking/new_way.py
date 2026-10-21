"""
Python 3.15: Unpacking in Comprehensions

The * operator unpacks items from each list.
This example flattens nested lists into one list.
"""

# Example data: products grouped by category.
product_groups = [
    ["Laptop", "Keyboard"],
    ["Mouse", "Monitor"],
    ["Headphones", "Webcam"],
]

print("Original data:")
print(product_groups)

# NEW WAY: Unpack each group inside a comprehension.
products = [*group for group in product_groups]

print("\nAll products:")
print(products)