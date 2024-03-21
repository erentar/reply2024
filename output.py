import os

OUTPUT_DIR = "./output/"


def output(state: dict[tuple: str], problem_name: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_DIR + problem_name + ".txt", "w") as f:
        for coord in state.keys():
            f.write(state[coord] + " " + str(coord[0]) + " " + str(coord[1]) + "\n")


if __name__ == "__main__":
    a = """
    3 3 4
    B 4 4
    C 4 3
    5 4 2
    A 5 2
    C 5 1
    5 5 0
    6 6 0
    C 6 1
    9 6 2
    F 7 3
    F 7 4
    F 7 5
    A 7 6
    9 5 6
    E 5 5
    6 5 4
    """
    b = output({
        (3, 4): "3",
        (4, 4): "B",
        (4, 3): "C",
        (5, 2): "A",
        (5, 1): "C",
        (5, 0): "5",
        (6, 0): "6",
        (6, 1): "C",
        (6, 2): "9",
        (7, 3): "F",
        (7, 4): "F",
        (7, 5): "F",
        (7, 6): "A",
        (5, 6): "9",
        (5, 5): "E",
        (5, 4): "6",
    },
        "exemple_test")
