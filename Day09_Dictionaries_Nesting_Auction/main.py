# The Python Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    # "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)


empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)


programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}


travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting Dictionary in a List

travel_log_3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]





