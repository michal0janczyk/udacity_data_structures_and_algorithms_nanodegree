class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items


def reverse_string(input_str):
    stack = Stack()
    result = ""

    for i in range(len(input_str)):
        stack.push(input_str[i])

    while not stack.is_empty():
        result += stack.pop()
    return result


if __name__ == "__main__":

    input_str = "!evitacudE ot emocleW"
    print(reverse_string(input_str))
