import math

def estimate_min_worst_case_length(data_length: int) -> int:
    n_possible_input_sequences = math.factorial(data_length)
    n_answer_sequences = 1
    min_worst_case_length = 0
    possible_operations = 11
    while n_answer_sequences < n_possible_input_sequences:
        min_worst_case_length += 1
        n_answer_sequences += possible_operations ** min_worst_case_length
    return min_worst_case_length

print("Minimal worst case scenario sorting length")
for i in range(11):
    print(f"{i:3}: {estimate_min_worst_case_length(i)}")
print(f"{100:3}: {estimate_min_worst_case_length(100)}")
print(f"{500:3}: {estimate_min_worst_case_length(500)}")
print(f"{1000:3}: {estimate_min_worst_case_length(1000)}")
print(f"{5000:3}: {estimate_min_worst_case_length(5000)}")
print(f"{10000:3}: {estimate_min_worst_case_length(10000)}")
