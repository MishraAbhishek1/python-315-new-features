"""
Python 3.15: Sentinel Values

A sentinel represents a special state, such as a missing value.
"""

# Create a special marker for a missing value.
MISSING = sentinel("MISSING")

# The default value is  Missing, not  None
def get_username(username=MISSING):
    
    # Check wether the caller provided a username.
    if username is MISSING:
        print("Username was not provided.")
    
    # None was explicitly provided.
    elif username is None:
        print("Username was explicitly set to None.")
    
    # A real username was provided.
    
    else:
        print("Username:", username)

# Example 1: No argument provided.
get_username()

# Example 2: Explicitly pass None.
get_username(None)

# Example 3: Pass a real username.
get_username("Abhishek")