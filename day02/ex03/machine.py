import random
from beverages import *


class CoffeeMachine:
    def __init__(self):
        self.empty_cup = CoffeeMachine.EmptyCup()
        self.count = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.count = 0

    def serve(self, cup: HotBeverage):
        if self.count < 10:
            self.count += 1
            i = random.randint(0, 1)
            if i == 0:
                return CoffeeMachine.EmptyCup()
            else:
                return type(cup)()
        else:
            raise CoffeeMachine.BrokenMachineException()


def main():
    machine = CoffeeMachine()
    for i in range(0, 6):
        try:
            print(machine.serve(Coffee()))
            print(machine.serve(Tea()))
            print(machine.serve(Chocolate()))
            print(machine.serve(Cappuccino()))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            machine.repair()


if __name__ == '__main__':
    main()
