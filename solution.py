import common
import argparse
import re

def day_1_puzzle_a(filename, debug):
    input = common.read_file(filename)
    list_len = len(input)
    input_list = common.strlist_to_intlist(input)
    input_list_cols = common.get_columns(input_list)
    input_list_cols_sorted = [sorted(x) for x in input_list_cols]
    distance = [abs(input_list_cols_sorted[0][i]-input_list_cols_sorted[1][i]) for i in range(list_len)]
    return sum(distance), input_list_cols

def day_1_puzzle_b(input_matrix, debug):
    similarity = [input_matrix[1].count(x)*x for x in input_matrix[0]]
    return sum(similarity)


def day_2_puzzle_a(filename, debug):
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

def day_2_puzzle_b(input_matrix, debug):
    diff_list = input_matrix[1]
    made_safe = input_matrix[2]

    for i, diff in enumerate(diff_list):
        if made_safe[i] == 0:
            positive_count = sum(1 for x in diff if x > 0)
            negative_count = sum(1 for x in diff if x < 0)
            zero_count = sum(1 for x in diff if x == 0)
            beyond_limit = sum(1 for x in diff if x > 3 or x < -3)
            beyond_limit_at_ends = sum(1 for x in [diff[0], diff[-1]] if x > 3 or x < -3)
            same_sign = bool(bool(positive_count)^bool(negative_count))

            beyond_limit_safe = False
            zero_safe = False
            if same_sign:
                beyond_limit_safe = beyond_limit == 1 and beyond_limit_at_ends == 1 and not zero_count
                zero_safe = zero_count == 1 and not beyond_limit
                
            if positive_count > negative_count:
                change_sign = negative_count == 1
            elif negative_count > positive_count:
                change_sign = positive_count == 1
            sign_safe = change_sign and not zero_count and not beyond_limit

            if sign_safe ^ zero_safe ^ beyond_limit_safe:
                made_safe[i] = 1
    return sum(made_safe)

def day_3_puzzle_a(filename, debug):
    input = common.read_file(filename)
    # Combine all the lines into a single string
    input = "".join(input)
    # Use regex get substrings that match three patterns: mul(d,d) where d is a digit, do(), or don't()
    valid_inst = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
    # Get the digits from the substrings in nx2 matrix if the string begings with mul, else return [1,0] if the string starts with do and [0,0] with the string starts with don't
    valid_num = [re.findall(r"\d+", x) if x.startswith("mul") else [0,0] for x in valid_inst]
    proceed = [[1,1] if x.startswith("do()") else [1,0] if x.startswith ("don't()") else [0,0] for x in valid_inst]
    # Convert the strings to integers
    valid_num = [[int(x) for x in y] for y in valid_num]
    # Get multiplication of the two numbers in each row
    answer = sum([x[0]*x[1] for x in valid_num])
    return answer, [valid_num, proceed]

def day_3_puzzle_b(input_matrix, debug):
    # Get first two columns of the input matrix
    valid_num = input_matrix[0]
    proceed = input_matrix[1]
    do_mult = True
    answer = 0
    for i, pair in enumerate(valid_num):
        prod = pair[0]*pair[1]
        # Check if do() [1,0]
        if proceed[i] == [1,1]:
            do_mult = True
        # Check if proceed
        elif proceed[i] == [1,0]:
            do_mult = False
        if do_mult:
            answer = answer + prod
    return answer

def day_4_puzzle_a(filename, debug):
    input = common.read_file(filename)
    counter = 0
    # For loop to match "XMAS"
    for i, word in enumerate(input):
        for j in range(len(word)):
            if word[j] == "X":
                # right
                if j+3 < len(word):
                    if word[j:j+4] == "XMAS":
                        counter += 1
                        if debug: print(f"[{i},{j}] right")
                # left
                if j-3 >= 0:
                    if word[j-3:j+1] == "SAMX":
                        counter += 1
                        if debug: print(f"[{i},{j}] left")
                # down
                if i+3 < len(input):
                    if input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] down")
                # up
                if i-3 >= 0:
                    if input[i-1][j] == "M" and input[i-2][j] == "A" and input[i-3][j] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] up")
                # diagonal right down
                if i+3 < len(input) and j+3 < len(word):
                    if input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] diagonal right down")
                # diagonal left down
                if i+3 < len(input) and j-3 >= 0:
                    if input[i+1][j-1] == "M" and input[i+2][j-2] == "A" and input[i+3][j-3] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] diagonal left down")
                # diagonal right up
                if i-3 >= 0 and j+3 < len(word):
                    if input[i-1][j+1] == "M" and input[i-2][j+2] == "A" and input[i-3][j+3] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] diagonal right up")
                # diagonal left up
                if i-3 >= 0 and j-3 >= 0:
                    if input[i-1][j-1] == "M" and input[i-2][j-2] == "A" and input[i-3][j-3] == "S":
                        counter += 1
                        if debug: print(f"[{i},{j}] diagonal left up")
    return counter, input

def day_4_puzzle_b(input_matrix, debug):
    counter = 0
    input = input_matrix
    for i, word in enumerate(input):
        for j in range(len(word)):
            left = False
            right = False
            if word[j] == "A" and i-1 >= 0 and i+1 < len(input) and j-1 >= 0 and j+1 < len(word):
                if input[i-1][j-1] == "M" and input[i+1][j+1] == "S":
                    left = True
                    if debug: print(f"[{i},{j}] left MAS")
                if input[i-1][j-1] == "S" and input[i+1][j+1] == "M":
                    left = True
                    if debug: print(f"[{i},{j}] left SAM")
                if input[i-1][j+1] == "M" and input[i+1][j-1] == "S":
                    right = True
                    if debug: print(f"[{i},{j}] right MAS")
                if input[i-1][j+1] == "S" and input[i+1][j-1] == "M":
                    right = True
                    if debug: print(f"[{i},{j}] right SAM")
                
                if left and right:
                    counter += 1
    answer = counter
    return answer

def day_5_puzzle_a(filename, debug):
    input = common.read_file(filename)
    rules = []
    updates = []
    rule_book = {}
    valid = []
    middle = []
    # Get strings in input with '|'
    for i, line in enumerate(input):
        if "|" in line:
            rules.append(line)
        elif "," in line:
            updates.append(line)
    if debug: print(f"DEBUG: Rules\n{rules}\nDEBUG: Updates\n{updates}")
    # Arrange list in ascending order
    rules.sort()
    if debug: print(f"DEBUG: Sorted rules\n{rules}")

    for rule in rules:
        # Split the rule into two parts
        parts = rule.split("|")
        ref = int(parts[0])
        rel = int(parts[1])

        if ref not in rule_book.keys():
            rule_book[ref] = {'before':[], 'after':[]}
        if rel not in rule_book.keys():
            rule_book[rel] = {'before':[], 'after':[]}

        rule_book[ref]['after'].append(rel)
        rule_book[rel]['before'].append(ref)
    if debug: print(f"DEBUG: Rule book\n{rule_book}")

    for i, update in enumerate(updates):
        # if debug: print(f"DEBUG: Update no. {i}")
        update_int = [int(x) for x in (update.split(","))]
        num_pages = len(update_int)
        for j, page in enumerate(update_int):
            # if debug: print(f"DEBUG: Page {page}")
            # Get elements in page before j
            before = update_int[0:j] if j > 0 else []
            after = update_int[j+1:] if j < num_pages else []
            # if debug: print(f"DEBUG: Update {i} page {page} Pages before {before}\nPages after {after}")

            if not set(before) & set(rule_book[page]['after']) and not set(after) & set(rule_book[page]['before']):
                if j == len(update_int)-1:
                    valid.append(True)
                    middle.append(update_int[int(num_pages/2)])
                    if debug: print(f"DEBUG: Update {i} is valid!")
            else:
                valid.append(False)
                middle.append(None)
                if debug: print(f"DEBUG: Update {i} is invalid because of page {page}")
                break
    if debug: print(f"DEBUG: Middle numbers\n{middle}")
    answer = sum([x for x in middle if x is not None])
    return answer, input







def day_X_puzzle_a(filename, debug):
    input = common.read_file(filename)
    answer = None
    return answer, input

def day_X_puzzle_b(input_matrix, debug):
    answer = None
    return answer

def main(day, mode="sample", puzzle="both", debug=False):
    if mode == "sample":
        filename = "day-" + day + "/sample.txt"
    else:
        filename = "day-" + day + "/input.txt"
    puzzleA, input_ = eval("day_" + day + "_puzzle_a(filename, debug)")
    answer = [puzzleA, None]
    print("Answer to puzzle A:", answer[0])
    
    if puzzle == "b" or puzzle == "both":
        answer = [puzzleA, eval("day_" + day + "_puzzle_b(input_, debug)")]
        print("Answer to puzzle B:", answer[1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument("--day", type=str, default="1", help="Day of the Advent of Code challenge")
    parser.add_argument("--mode", type=str, default="sample", help="Mode to run the solution (sample or input)")
    parser.add_argument("--puzzle", type=str, default="a", help="Puzzle to solve (a or b)")
    parser.add_argument("--debug", action="store_true", help="Print debug information")
    
    args = parser.parse_args()
    main(day=args.day, mode=args.mode, puzzle=args.puzzle, debug=args.debug)