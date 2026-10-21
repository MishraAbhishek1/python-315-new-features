"""
NEW WAY: Using frozendict in Python 3.15

A normal dictionary (dict) is mutable, meaning its data can be
changed after creation.

Python 3.15 introduces frozendict, an immutable dictionary.
Once created, its key-value mappings cannot be modified.

Let's see how this helps protect shared configuration
in a backend application.
"""

# Step 1: Create an immutable application configuration.
from builtins import frozendict

app_config = frozendict({
    "app_name": "My SaaS Application",
    "debug": False,
    "max_connections": 100,
})

print("Initial configuration:")
print(app_config)


# Step 2: Imagine two backend services share the same configuration.
# Both variables reference the SAME frozendict object.

service_a_config = app_config
service_b_config = app_config


# Step 3: Service A attempts to modify the shared configuration.
# Unlike a normal dictionary, frozendict does not allow this change.


try:
    service_a_config["debug"] = True
except TypeError as error:
    print("\nService A cannot modify the configuration:")
    print(error)


# Step 4: Check the configuration used by Service B.
# Its configuration remains unchanged.

print("\nConfiguration used by Service B:")
print(service_b_config)


# Step 5: Check whether both services reference the same object.

print("\nAre both configurations the same object?")
print(service_a_config is service_b_config)