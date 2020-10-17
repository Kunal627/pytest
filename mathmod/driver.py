import sys
from pathlib import Path 
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from mathclass import MathClass
# Driver Code 
math = MathClass()
print(math.factorial(5))
print(math.square(3))