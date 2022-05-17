import sys


def main():
    if len(sys.argv) != 2:
        sys.exit()
    s = sys.argv[1].split(",")
    for word in s:
        input_word = word.strip(" ")
        if len(input_word) > 0:
            func(input_word)


def func(word):
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
    capital = get_capital(word, states, capital_cities)
    state = get_state(word, states, capital_cities)
    if capital:
        print(f"{word.title()} is the capital of {capital}")
    elif state:
        print(f"{state} is the capital of {word.title()}")
    else:
        print(f"{word} is neither a capital city nor a state")


def get_capital(word, states, capital_cities):
    key_state = None
    for key, value in capital_cities.items():
        if value.lower() == word.lower().strip():
            key_state = key
    if key_state:
        for key, value in states.items():
            if key_state.lower() == value.lower():
                return key
    return None


def get_state(word, states, capital_cities):
    key_state = None
    for key in states.keys():
        if key.lower() == word.lower().strip():
            key_state = states[key]
    if key_state:
        for key in capital_cities.keys():
            if key_state.lower() == key.lower():
                return capital_cities[key]
    return None


if __name__ == '__main__':
    main()
