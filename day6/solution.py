class Solution:
    @staticmethod
    def get_input(path: str) -> str:
        with open(path, "r") as f:
            return f.read()

    @staticmethod
    def chunks(s: str, n: int):
        for i in range(0, len(s)):
            if len(s[i : i + n]) == n:
                yield (i, s[i : i + n])

    @staticmethod
    def check_valid(s: str, n: int) -> bool:
        counts = []
        for i in range(n):
            counts.append(s.count(s[i]))
        return all([c == 1 for c in counts])

    @staticmethod
    def task1():
        input = Solution.get_input("input.txt")
        mapping = {
            idx: Solution.check_valid(chunk, 4)
            for idx, chunk in list(Solution.chunks(input, 4))
        }
        for idx, valid in mapping.items():
            if valid:
                print(idx + 4)
                break

    @staticmethod
    def task2():
        input = Solution.get_input("input.txt")
        mapping = {
            idx: Solution.check_valid(chunk, 14)
            for idx, chunk in list(Solution.chunks(input, 14))
        }
        for idx, valid in mapping.items():
            if valid:
                print(idx + 14)
                break


if __name__ == "__main__":
    Solution.task1()
    Solution.task2()
