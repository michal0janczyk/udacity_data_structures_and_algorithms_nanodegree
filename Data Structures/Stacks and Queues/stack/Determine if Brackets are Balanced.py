class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for char in equation:
        if char in "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() == None:
                return False

    if stack.size() == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Base cases:")
    print("Pass" if (equation_checker("((3))")) else "Fail")
    print("Pass" if (equation_checker("(()")) else "Fail")
    print("Equation:")
    print("Pass" if (equation_checker("((3^2 + 8)*(5/2))/(2+6)")) else "Fail")
    print(
        "Pass" if not (equation_checker("((3^2 + 8)*(5/2))/(2+6))")) else "Fail"
    )
