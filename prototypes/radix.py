from collections import deque

def dummy_simplify(data: list[int]) -> list[int]:
    indexed = list(enumerate(data))
    indexed.sort(key=lambda x : x[1])
    ans = [0] * len(data)
    for val, old_pos in enumerate(indexed):
        ans[old_pos[0]] = val
    return ans

def dummy_radix_sort_steps(data: list[int]) -> list[str]:
    data = dummy_simplify(data)
    element_count = len(data)
    a = deque(data)
    b = deque()
    bit = 1
    ans = []
    while bit <= element_count:
        pos = 0
        while pos < element_count:
            if a[0] & bit:
                a.append(a.popleft())
                ans.append("ra")
            else:
                b.appendleft(a.popleft())
                ans.append("pb")
            pos += 1
        while len(b) > 0:
            a.appendleft(b.popleft())
            ans.append("pa")
        bit = bit << 1
    return ans

def get_number_cost(number: int, n_digits: int) -> int:
    '''
    returns cost i. e. number of operations on number
    during ternary radix sort with n_digits phases
    >>> get_number_cost(0, 1)
    4
    >>> get_number_cost(0, 2)
    8
    >>> get_number_cost(4, 2)
    4
    '''
    digit_costs = {0: 4, 1: 2, 2: 1}
    cost = 0
    for i in range(n_digits):
        cost += digit_costs[number % 3]
        number //= 3
    return cost

def get_best_n_digits_data_to_sort(data_length: int, n_digits: int) -> list[int]:
    return sorted(list(range(3 ** n_digits)),
                key=lambda x : get_number_cost(x, n_digits))[:data_length]

def get_data_cost(data: list[int], n_digits: int) -> int:
    return sum(map(lambda x : get_number_cost(x, n_digits), data))

def get_minimum_required_n_digits(data_length: int):
    n_digits = 1
    n_numbers = 3
    while n_numbers < data_length:
        n_digits += 1
        n_numbers *= 3
    return n_digits

def get_n_digits_in_number(number: int):
    assert(number >= 0)
    ans = 1
    while 3 ** ans <= number:
        ans += 1
    return ans

def get_best_data_to_sort(data_length: int) -> list[int]:
    '''
    returns sorted list of numbers optimized for sorting with radix sort base 3
    >>> get_best_data_to_sort(4)
    [4, 5, 7, 8]
    '''
    minimum_required_n_digits = get_minimum_required_n_digits(data_length)
    best_n_digits = minimum_required_n_digits
    best_data = get_best_n_digits_data_to_sort(data_length, best_n_digits)
    best_cost = get_data_cost(best_data, best_n_digits)
    for n_digits in range(minimum_required_n_digits + 1, minimum_required_n_digits + 3):
        data = get_best_n_digits_data_to_sort(data_length, n_digits)
        cost = get_data_cost(data, n_digits)
        if cost < best_cost:
            best_data = data
            best_cost = cost
    return sorted(best_data)

def smart_simplify(data: list[int]) -> list[int]:
    '''
    returns list of numbers that requires identical operations to sort
    but is optimized for ternary radix sort
    >>> smart_simplify([-5, 10, 7, 3])
    [4, 8, 7, 5]
    '''
    simple_numbers = get_best_data_to_sort(len(data))
    indexed = list(enumerate(data))
    indexed.sort(key=lambda x : x[1])
    ans = [0] * len(data)
    for new_val_pos, old_pos in enumerate(indexed):
        ans[old_pos[0]] = simple_numbers[new_val_pos]
    return ans

def ternary_radix_sort_steps(data: list[int]) -> list[str]:
    data = smart_simplify(data)
    n_digits = get_n_digits_in_number(max(data))
    a = deque(data)
    b = deque()
    ans = []
    for step in range(n_digits):
        pos = 0
        count_0 = 0
        count_1 = 0
        while pos < len(data):
            if a[0] % 3 == 2:
                a.append(a.popleft() // 3)
                ans.append("ra")
            elif a[0] % 3 == 1:
                b.appendleft(a.popleft() // 3)
                ans.append("pb")
                count_1 += 1
            else:
                b.append(a.popleft() // 3)
                ans.extend(["pb", "rb"])
                count_0 += 1
            pos += 1
        for i_0 in range(count_1):
            a.appendleft(b.popleft())
            ans.append("pa")
        for i_1 in range(count_0):
            a.appendleft(b.pop())
            if i_1 < count_0 - 1:
                ans.append("rrb")
            ans.append("pa")
        assert(len(b) == 0)
        assert(len(a) == len(data))
    return ans

if __name__ == "__main__":
    import doctest
    doctest.testmod()
