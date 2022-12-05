from typing import Dict, List
import copy


class Stack:
    def __init__(self, stack: List[str]):
        self.stack = stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push_multiple(self, items: List[str]):
        for item in items:
            self.push(item)

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def __iter__(self):
        return iter(self.stack)


CARGO = {
    "1": Stack(["B", "P", "N", "Q", "H", "D", "R", "T"]),
    "2": Stack(["W", "G", "B", "J", "T", "V"]),
    "3": Stack(["N", "R", "H", "D", "S", "V", "M", "Q"]),
    "4": Stack(["P", "Z", "N", "M", "C"]),
    "5": Stack(["D", "Z", "B"]),
    "6": Stack(["V", "C", "W", "Z"]),
    "7": Stack(["G", "Z", "N", "C", "V", "Q", "L", "S"]),
    "8": Stack(["L", "G", "J", "M", "D", "N", "V"]),
    "9": Stack(["T", "P", "M", "F", "Z", "C", "G"]),
}


class Solution:
    @staticmethod
    def get_input(path: str) -> List[str]:
        with open(path, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def parse(input: List[str]) -> List[List[str]]:
        parsed = []
        temp = []
        for line in input:
            for word in line.split(" "):
                if word.isdigit():
                    temp.append(word)
            parsed.append((temp[0], temp[1], temp[2]))
            temp = []
        return parsed  # amount, from, to

    @staticmethod
    def move_stacks(amount: int, from_stack: Stack, to_stack: Stack):
        for _ in range(amount):
            to_stack.push(from_stack.pop())

    @staticmethod
    def move_as_batch(amount: int, from_stack: Stack, to_stack: Stack):
        move = [from_stack.pop() for _ in range(amount)][::-1]
        to_stack.push_multiple(move)

    @staticmethod
    def task1():
        cargo = copy.deepcopy(CARGO)
        input = Solution.get_input("input.txt")
        parsed = Solution.parse(input)
        for amount, from_stack, to_stack in parsed:
            Solution.move_stacks(int(amount), cargo[from_stack], cargo[to_stack])
        return "".join([val.peek() for _, val in cargo.items()])

    @staticmethod
    def task2():
        cargo = copy.deepcopy(CARGO)
        input = Solution.get_input("input.txt")
        parsed = Solution.parse(input)
        for amount, from_stack, to_stack in parsed:
            Solution.move_as_batch(int(amount), cargo[from_stack], cargo[to_stack])
        return "".join([val.peek() for _, val in cargo.items()])


if __name__ == "__main__":
    print("Task 1:", Solution.task1())
    print("Task 2:", Solution.task2())
