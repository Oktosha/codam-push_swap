from itertools import permutations
from prototypes.small import solve, State
from check import grade


def check_solutions_for_length(length: int) -> int:
    print(f"solving length={length}")
    answer = solve(length)
    maximum_steps = 0
    for data in permutations(list(range(length))):
        state = State(a=tuple(data), b=())
        if state not in answer:
            print(f"NO SOLUTION for {data}!")
            return -1
        else:
            steps = answer[state]
            current_grade = grade(data, steps)
            if current_grade.correctness == True:
                maximum_steps = max(maximum_steps, current_grade.length)
            elif current_grade.correctness == None:
                print(f"checker failure for {data}!")
                print(f"the answer was {steps}")
                return -2
            elif current_grade.correctness == False:
                print(f"wrong answer for {data}!")
                return -3
    return maximum_steps


for length in range(1, 9):
    maximum_steps = check_solutions_for_length(length)
    if maximum_steps < 0:
        print(f"Failed at length {length}")
        break
    else:
        print(f"max steps at length {length} = {maximum_steps}")


def pretty_print_dp_results(results: dict[State, list[str]], show_helper_states: bool = False):
    keys = list(results.keys())
    if not show_helper_states:
        keys = filter(lambda state: len(state.b) == 0, keys)
    for key in sorted(keys):
        print(key.a, results[key])

pretty_print_dp_results(solve(3))
