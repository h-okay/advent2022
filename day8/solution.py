import numpy as np


def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        split = [int(num) for row in data for num in row]
        return np.array(split).reshape(99, 99)


def check_if_visible(data, position):
    row, column = position
    if (  # edges
        row == 0
        or row == data.shape[0] - 1
        or column == 0
        or column == data.shape[1] - 1
    ):
        return True
    return any(
        [
            data[row, column] > data[:row, column].max(),
            data[row, column] > data[row + 1 :, column].max(),
            data[row, column] > data[row, :column].max(),
            data[row, column] > data[row, column + 1 :].max(),
        ]
    )


def how_many_trees_until_blocked(selection, path):
    count = 0
    for tree in path:
        count += 1
        if selection > tree:
            continue
        break
    return count


def get_scene_score(data, position):
    row, column = position
    above = how_many_trees_until_blocked(data[row, column], data[:row, column][::-1])
    below = how_many_trees_until_blocked(data[row, column], data[row + 1 :, column])
    left = how_many_trees_until_blocked(data[row, column], data[row, :column][::-1])
    right = how_many_trees_until_blocked(data[row, column], data[row, column + 1 :])
    return above * below * left * right


def task1():
    data = get_input()
    count = 0
    for x, y in np.ndindex(data.shape):
        if check_if_visible(data, (x, y)):
            count += 1
    print("total visible", count)


def task2():
    data = get_input()
    max_score = 0
    for x, y in np.ndindex(data.shape):
        max_score = np.amax([max_score, get_scene_score(data, (x, y))])
    print("max score", max_score)


if __name__ == "__main__":
    task1()
    task2()
