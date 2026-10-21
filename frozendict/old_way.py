"""
BEFORE: Using a normal Python dictionary (dict)

A normal dictionary is MUTABLE, which means we can change,
add, or remove its data after creating it.

Let's understand how this behavior can cause problems
in a production backend application.
"""


# Step 1: Create application configuration
app_config = {
    "app_name": "My Saas Aplication",
    "debug": False,
    "max_connections": 100,
}

print("Initial configuratinos")
print(app_config)

# Step 2: Imagine two backend services use the same configuration.
# Both variables point to the SAME dictionary object.

service_a_config = app_config
service_b_config = app_config

service_a_config["debug"] = True
service_a_config["max_connections"] = 500


# Step 4: Check the configuration used by Service B.
# Service B can also see the changes made by Service A.

print("\nConfiguration used by Service B:")
print(service_b_config)


# Step 5: Check whether both variables reference the same object.

print("\nAre both configurations the same object?")
print(service_a_config is service_b_config)