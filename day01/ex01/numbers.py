def fun():
    with open("numbers.txt", "r") as file:
        data = file.read()
        array = data.split(",")
        for number in array:
            print(number.strip("\n"))


if __name__ == '__main__':
    fun()
