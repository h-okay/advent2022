import string
from typing import List, Set, Tuple

priorities = {val: i+ 1 for i, val in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

class Solution:
    @staticmethod
    def get_input(path: str) -> List[str]:
        with open(path, "r") as file:
            return file.read().splitlines()
        
    @staticmethod
    def split_parts(input: List[str]) -> List[Tuple[str]]:
        all_parts = []
        for rucksack in input:
            idx = len(rucksack) // 2
            compartment1 = rucksack[:idx]
            compartment2 = rucksack[idx:]
            all_parts.append((compartment1, compartment2))
        return all_parts
    
    @staticmethod
    def split_groups(input: List[str], group_size: int = 3) -> List[Tuple[str]]:
        for i in range(0, len(input), group_size):
            yield input[i:i+group_size]

    @staticmethod
    def find_badges(rucksak1: str, rucksack2: str, rucksack3: str) -> Set[str]:
        badges = set()
        for char in string.ascii_lowercase + string.ascii_uppercase:
            if char in rucksak1 and char in rucksack2 and char in rucksack3:
                badges.add(char)
        return badges
        
    @staticmethod
    def find_matching_items(compartment1: str, compartment2: str) -> Set[str]:
        result = []
        for item1 in compartment1:
            for item2 in compartment2:
                if item1 == item2:
                    result.append(item1)
        return set(result)

    @staticmethod
    def convert_to_prio(items: List[Set[str]]) -> List[int]:
        return [priorities[char] for item in items for char in item]

    @staticmethod
    def calculate(items: Set[str]) -> int:
        result = 0
        for item in items:
            result += priorities[item]
        return result

    @staticmethod
    def task1():
        input = Solution.get_input("input.txt")
        parts = Solution.split_parts(input)
        matching = [Solution.find_matching_items(part[0], part[1]) for part in parts]
        prios = Solution.convert_to_prio(matching)
        return sum(prios)

    @staticmethod
    def task2():
        input = Solution.get_input("input.txt")
        split_groups = Solution.split_groups(input)
        badges = [Solution.find_badges(group[0], group[1], group[2]) for group in list(split_groups)]
        prios = Solution.convert_to_prio(badges)
        return sum(prios)

if __name__ == "__main__":
    print("Task 1:", Solution.task1())
    print("Task 2:", Solution.task2())
    
    
