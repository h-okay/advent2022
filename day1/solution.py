from typing import List


class Solution:
    @staticmethod
    def get_input(path: str) -> List[str]:
        with open(path, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def parse(input: List[str]) -> List[List[int]]:
        all_values = []
        temp = []
        for line in input:
            if line == "":
                all_values.append(temp)
                temp = []
                continue
            temp.append(int(line))
        all_values.append(temp)
        return all_values

    @staticmethod
    def calculate(values: List[List[int]]) -> List[int]:
        result = []
        for value in values:
            result.append(sum(value))
        return result

    @staticmethod
    def max_value(values: List[int]) -> int:
        return max(values)

    @staticmethod
    def top_3_value(values: List[int]) -> int:
        values.sort(reverse=True)
        return values[0] + values[1] + values[2]

    def task1(self, path: str) -> int:
        input = self.get_input(path)
        values = self.parse(input)
        result = self.calculate(values)
        return self.max_value(result)

    def task2(self, path: str) -> int:
        input = self.get_input(path)
        values = self.parse(input)
        result = self.calculate(values)
        return self.top_3_value(result)


if __name__ == "__main__":
    solution = Solution()
    print("First:", solution.task1("input.txt"))
    print("Top 3:", solution.task2("input.txt"))
