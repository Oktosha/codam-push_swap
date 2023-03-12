from prototypes.merge import dummy_merge_sort_steps
from prototypes.radix import dummy_radix_sort_steps
from check import grade

for algo in [dummy_merge_sort_steps, dummy_radix_sort_steps]:
    print(algo.__name__, end=": ")
    for count in [100, 500, 1000]:
        data = list(reversed(range(count)))
        current_grade = grade(data, algo(data))
        print(f"{count}={current_grade}", end="; ")
    print()
