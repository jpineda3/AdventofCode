import common
import argparse

def day_1_puzzle_a(filename):
    input = common.read_file(filename)
    list_len = len(input)
    input_list = common.strlist_to_intlist(input)
    input_list_cols = common.get_columns(input_list)
    input_list_cols_sorted = [sorted(x) for x in input_list_cols]
    distance = [abs(input_list_cols_sorted[0][i]-input_list_cols_sorted[1][i]) for i in range(list_len)]
    return sum(distance), input_list_cols

def day_1_puzzle_b(input_matrix):
    similarity = [input_matrix[1].count(x)*x for x in input_matrix[0]]
    return sum(similarity)

def main(day, mode="sample"):
    if mode == "sample":
        filename = "day-" + day + "-sample.txt"
    else:
        filename = "day-" + day + "-input.txt"
    puzzleA, input_ = eval("day_" + day + "_puzzle_a(filename)")
    answer = [puzzleA, eval("day_" + day + "_puzzle_b(input_)")]
    print("Answer to puzzle A:", answer[0])
    print("Answer to puzzle B:", answer[1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument("--day", type=str, default="1", help="Day of the Advent of Code challenge")
    parser.add_argument("--mode", type=str, default="sample", help="Mode to run the solution (sample or input)")

    args = parser.parse_args()
    main(day=args.day, mode=args.mode)