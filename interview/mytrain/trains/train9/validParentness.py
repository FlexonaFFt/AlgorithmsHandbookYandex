class Validator:
    def ParentnessWorker(self, sequence: str) -> bool:
        start= ['(', '[', '{']
        pair = {')': '(', ']': '[', '}': '{'}
        current_sub_stack = []

        for element in sequence:
            if element in start:
                current_sub_stack.append(element)
            else:
                if not current_sub_stack:
                    return False
                if current_sub_stack[-1] != pair.get(element):
                    return False
                current_sub_stack.pop()
        return len(current_sub_stack) == 0


if __name__ == '__main__':
    print(Validator().ParentnessWorker("([{}])"))
    print(Validator().ParentnessWorker("()[]{}"))
    print(Validator().ParentnessWorker(('({')))