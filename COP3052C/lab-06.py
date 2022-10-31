"""COP3502C: LAB 06"""


def add(x: float, y: float) -> float:
    """Adds two numbers together."""

    return x + y


def main() -> None:
    x, y = 5.0, 3.0

    print(add(x, y))


if __name__ == '__main__':
    main()
