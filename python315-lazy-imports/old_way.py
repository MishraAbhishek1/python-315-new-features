"""
OLD WAY: Normal import in Python

Python loads the json module when it reaches the import statement.
"""

import json

print("Program started")

# use json to covert a  python dictionary into a json String.

data  = {"name":"abhishek", "role": "Python Developer"}

result = json.dumps(data)

print("Json Data:", result)