from collections import deque
from itertools import permutations

def simplify(data: list[int]) -> list[int]:
    indexed = list(enumerate(data))
    indexed.sort(key=lambda x : x[1])
    ans = [0] * len(data)
    for val, old_pos in enumerate(indexed):
        ans[old_pos[0]] = val
    return ans

def dummy_radix_sort_steps(data: list[int]) -> list[str]:
    data = simplify(data)
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