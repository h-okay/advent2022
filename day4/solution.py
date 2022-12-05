from typing import List, Set


class Solution:
    @staticmethod
    def get_input(path: str) -> List[str]:
        with open(path, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def split_assignments(input: List[str]) -> List[List[str]]:
        assignments = []
        for line in input:
            a1, a2 = line.split(",")
            assignments.append((a1.strip(), a2.strip()))
        return assignments

    @staticmethod
    def get_range(delimiter: str, assignment: str) -> range:
        start, end = assignment.split(delimiter)
        return range(int(start), int(end) + 1)

    @staticmethod
    def is_subset(a1: Set[int], a2: Set[int]) -> bool:
        return a1.issubset(a2) or a2.issubset(a1)

    @staticmethod
    def how_many_subsets(assignments: List[List[str]]) -> int:
        count = 0
        for a1, a2 in assignments:
            r1 = set(Solution.get_range("-", a1))
            r2 = set(Solution.get_range("-", a2))
            if Solution.is_subset(r1, r2):
                count += 1
        return count

    @staticmethod
    def does_ranges_overlap(a1: Set[int], a2: Set[int]) -> bool:
        return len(a1.intersection(a2)) > 0

    @staticmethod
    def how_many_overlaps(assignments: List[List[str]]) -> int:
        count = 0
        for a1, a2 in assignments:
            r1 = set(Solution.get_range("-", a1))
            r2 = set(Solution.get_range("-", a2))
            if Solution.does_ranges_overlap(r1, r2):
                count += 1
        return count

    @staticmethod
    def task1(path: str) -> int:
        input = Solution.get_input(path)
        assignments = Solution.split_assignments(input)
        return Solution.how_many_subsets(assignments)

    @staticmethod
    def task2(path: str) -> int:
        input = Solution.get_input(path)
        assignments = Solution.split_assignments(input)
        return Solution.how_many_overlaps(assignments)


if __name__ == "__main__":
    print("Task 1:", Solution.task1("input.txt"))
    print("Task 2:", Solution.task2("input.txt"))
