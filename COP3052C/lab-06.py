"""COP3502C: LAB 06"""


def add(x: float, y: float) -> float:
    """Adds two numbers."""

    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""

    return x - y


def main() -> None:
    x, y = 5.0, 3.0

    print(add(x, y))
    print(subtract(x, y))


if __name__ == '__main__':
    main()
