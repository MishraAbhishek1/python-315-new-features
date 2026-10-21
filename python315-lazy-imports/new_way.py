"""
NEW WAY: Lazy imports in Python 3.15

Python delays loading the json module until we use it.
"""
# Python 3.15 feature: lazy import
lazy import json

import sys

print("Program Started")

# Check wether json has been loaded.
print("Before using json:", "json" in sys.modules)

# Now we use josn for the first time.
data = {"name": "Abhishek", "role": "Python Developer"}

result = json.dumps(data)

print("JSON data:", result)

# json is now loaded
print("After using json:", "json" in sys.modules)