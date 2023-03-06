import sys
from collections import deque

a = []
for arg in sys.argv[1:]:
    a.extend(map(int, arg.split()))
#print(a)

if len(a) == 0:
    a = [x for x in range(1000000)]
    a.reverse()

print(f"check; a[0] = {a[0]}, a[-1] = {a[-1]}")
a = deque(a)
element_count = len(a)
sorted_length = 1
b = deque()
ans = []
while sorted_length < element_count:
    pos = 0
    while pos < element_count:
        current_segment_length = min(sorted_length * 2, element_count - pos)
        first_half_length = min(element_count - pos, sorted_length)
        second_half_length = current_segment_length - first_half_length
        if second_half_length > 0:
            for i in range(first_half_length):
                ans.append("pb")
                ans.append("rb")
                b.append(a.popleft())
            pos_a = 0
            while pos_a < second_half_length or len(b) > 0:
                if len(b) == 0 or (pos_a < second_half_length and a[0] < b[0]):
                    ans.append("ra")
                    a.append(a.popleft())
                    pos_a += 1
                else:
                    ans.append("pa")
                    ans.append("ra")
                    a.append(b.popleft())
        else:
            ans.extend(["ra"] * current_segment_length)
            # a = a[current_segment_length:] + a[:current_segment_length]
            a.rotate(-current_segment_length)
        pos += current_segment_length
    sorted_length *= 2

# print(a)
# print("\n".join(ans))
print(len(ans))
