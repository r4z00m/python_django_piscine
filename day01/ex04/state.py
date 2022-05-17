import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    key_state = None
    city = sys.argv[1]
    for key, value in capital_cities.items():
        if value == city:
            key_state = key
    if key_state:
        for key, value in states.items():
            if key_state == value:
                print(key)
                sys.exit()
    print("Unknown capital city")


if __name__ == '__main__':
    main()
