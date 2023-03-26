travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country (country, number_of_visits, cities, my_travel_log):
    my_travel_log.append(
        {
            "country": country,
            "visits": number_of_visits,
            "cities": cities,
        },
    )

    print(f"You've visited {country} {number_of_visits} times.")
    print(f"You've been to {cities}.")


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"], travel_log)

print(travel_log)
