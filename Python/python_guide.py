from dataclasses import dataclass, field, astuple, asdict
from typing import List

"""
**************************************

			DATACLASSES

**************************************

frozen - makes the object immutable (so that it
		 can be used as key in ditcionaries)
order - makes the instances comparable as tuples
		with the arguments in the same order as they
		are presented in the class
"""
@dataclass(frozen=True, order=True)
class Comment:
	id: int
	text: str = ""
	replies: List[int] = field(default_factory=list, compare=False, hash=False, repr=False)


com1 = Comment(1, "some text")
print(com1)  			# Comment(id=1, text='some text') 	
print(astuple(com1))	# (1, 'some text', [])
print(asdict(com1))		# {'id': 1, 'text': 'some text', 'replies': []}


"""
**************************************

				PEP8

**************************************
"""
# variables should be snake case
my_var = 1
i, x, a, b = 0, 0, 0, 0

# constants should be all upper case
CONSTANT = 1

# whitespaces - spaces can be removed in order
# to show the order of operations
i = i + 1
x = x*2 - 1
c = (a+b) * (a-b)

# in-line comments
COLOR = (0, 255, 0)  # This is correct
COLOR = (0, 255, 0) # This is incorrect



"""
ADD DATACLASES AND MATPLOTLIB

Extras:
	- NamedTuple
P.S.: sorry for all caps
"""