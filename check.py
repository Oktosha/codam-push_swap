from plumbum import local
from typing import Optional
from prototypes.merge import dummy_merge_sort_steps

class Grade():
	def __init__(self, length: int, correctness: Optional[bool]):
		self.length = length
		# True - solution is correct
		# False - solution is incorrect
		# None - failed to run the checker
		self.correctness = correctness
	def __str__(self):
		correctness_str = "[??]"
		if self.correctness == True:
			correctness_str = "[OK]"
		if self.correctness == False:
			correctness_str = "[WA]"
		return correctness_str + " " + str(self.length)

def grade(data: list[int], solution: list[str]) -> Grade:
	try:
		checker = local["./checker"]
		data_as_str = " ".join(map(str, data))
		solution_as_str = ""
		if len(solution) > 0:
			solution_as_str = "\n".join(solution) + "\n"
		grade_result = (checker[data_as_str] << solution_as_str).run(retcode = None)
		if grade_result[0] == 0:
			return Grade(len(solution), True)
		return Grade(len(solution), False)
	except:
		return Grade(len(solution), None)
