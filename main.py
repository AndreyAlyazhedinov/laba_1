"""Калькулятор"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Калькулятор")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"67 - 52 = {subtract(67, 52)}")


if __name__ == "__main__":
    main()
