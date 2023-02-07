travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
]

def new_country():
    country = input("Please enter the country you visited: ")
    visits = input("Please enter the number of visits you did: ")
    cities = input("Please enter the number of cities you visited: ").split()

    new_country_dict = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country_dict)
    print(travel_log)

new_country()