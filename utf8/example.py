"""
Python 3.15: UTF-8 as the Default Encoding

Python 3.15 uses UTF-8 by default when opening text files
without specifying an encoding.
"""

from pathlib import Path

# Create a text file containing multilingual text.
file_path = Path("utf8/sample.txt")

text = "Hello! नमस्ते! café! 🚀"

# Python 3.15: UTF-8 is the default encoding.
with open(file_path, "w") as file:
    file.write(text)

print("Text written successfully!")

# Read the text back from the file.
with open(file_path, "r") as file:
    content = file.read()

print("Text read from file:")
print(content)

# Check the default encoding of text files.
with open(file_path, "r") as file:
    print("File encoding:", file.encoding)