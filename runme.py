from prototypes.merge import dummy_merge_sort_steps
from check import grade


data = [5, 4, 3, 2, 1]
solution = dummy_merge_sort_steps(data)
print (f"Dummy merge sort for {data}")
print(grade(data, dummy_merge_sort_steps(data)))
