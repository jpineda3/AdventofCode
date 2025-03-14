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


def day_2_puzzle_a(filename):
    input = common.read_file(filename)
    input_list = common.strlist_to_intlist(input)
    safety = [] * len(input_list)
    diff_list = [] * len(input_list)
    for report in input_list:
        # Get difference between adjacent elements in report
        diff = [report[i+1] - report[i] for i in range(len(report)-1)]
        diff_list.append(diff)
        # Check if every element has the same sign
        if all(x > 0 for x in diff) or all(x < 0 for x in diff):
            # Check if all elements are within are within the range [1,3]
            if all(abs(x)>=1 and abs(x) <= 3  for x in diff):
                safety.append(1)
            else:
                safety.append(0)
        else:
            safety.append(0)
    return sum(safety), [input_list, diff_list, safety]


def main(day, mode="sample", puzzle="both"):
    if mode == "sample":
        filename = "day-" + day + "/sample.txt"
    else:
        filename = "day-" + day + "/input.txt"
    puzzleA, input_ = eval("day_" + day + "_puzzle_a(filename)")
    answer = [puzzleA, None]
    print("Answer to puzzle A:", answer[0])
    
    if puzzle == "b" or puzzle == "both":
        answer = [puzzleA, eval("day_" + day + "_puzzle_b(input_)")]
        print("Answer to puzzle B:", answer[1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument("--day", type=str, default="1", help="Day of the Advent of Code challenge")
    parser.add_argument("--mode", type=str, default="sample", help="Mode to run the solution (sample or input)")
    parser.add_argument("--puzzle", type=str, default="both", help="Puzzle to solve (a or b)")

    args = parser.parse_args()
    main(day=args.day, mode=args.mode, puzzle=args.puzzle)