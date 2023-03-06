from prototypes.merge import dummy_merge_sort_steps
from plumbum import local

raw_data = "5 4 6 3 2 1"
ls = local["ls"]
print(ls())
