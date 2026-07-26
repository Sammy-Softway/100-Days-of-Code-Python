from pandas.tseries.frequencies import key


def add(*args):
    print(args)
    return sum(args)

def calculate(**kwargs):
    print(kwargs)

def calculate_2(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

def calculate_3(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

print(add(1,2,3,4,5,6))
print("\n")
calculate(a=1, b=2, c=3)
print("\n")
calculate_2(a=1, b=2, c=3)
print("\n")
calculate_3(1, add=2, multiply=3)

class Car:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.price = kwargs.get("price")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

my_car = Car(name="Bugatti", model="Ph-500w", color="blue")
print(my_car.name)
print(my_car.price)
print(my_car.model)
print(my_car.color)