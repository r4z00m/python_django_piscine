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
    for key in states.keys():
        if key == city:
            key_state = states[key]
    if key_state:
        for key in capital_cities.keys():
            if key_state == key:
                print(capital_cities[key])
                sys.exit()
    print("Unknown state")


if __name__ == '__main__':
    main()
