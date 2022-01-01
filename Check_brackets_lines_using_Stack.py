class Stack:

    def __init__(self, input_list):
        self.input_list = input_list

    def is_empty(self):
        return self.input_list == list

    def push(self, elem):
        self.input_list.insert(0, elem)

    def pop(self):
        return self.input_list.pop(0)

    def peek(self):
        return self.input_list[0]

    def size(self):
        return len(self.input_list)


def check_brackets_line(input_line):
    stack = Stack([list])
    key_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    index = 0

    for elem in input_line:
        index += 1
        if elem not in key_dict.keys():
            stack.push(elem)
        elif stack.is_empty():
            return 'Unbalanced'
        elif key_dict[elem] == stack.peek():
            stack.pop()
        else:
            return 'Unbalanced'
    return 'Balanced'


if __name__ == '__main__':
    print(check_brackets_line('(((([{}]))))'))
    print(check_brackets_line('[([])((([[[]]])))]{()}'))
    print(check_brackets_line('{{[()]}}'))
    print(check_brackets_line('}{}'))
    print(check_brackets_line('{{[(])]}}'))
    print(check_brackets_line('[[{())}]'))
