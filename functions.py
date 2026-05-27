def multiply(a, b):
    """Multiplies two numbers."""
    return a * b
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(multiply(number, 2))

def get_bio(**bio):
    print(bio)
    get_bio(name="John Doe", age=30, profession="Software Developer")
    print("This is a simple function to demonstrate **kwargs in Python.")


def greeting(hello_world):
    """Prints a greeting message."""
    print(hello_world)

greeting("Hello, World!")

greet()

#global valiable
AGE = 18
def greet():
    name = "geff"
    print(f"Hello, {name}, you are {AGE} years old.")

greet()