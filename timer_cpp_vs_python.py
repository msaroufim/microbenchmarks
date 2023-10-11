import torch
from torch.utils.benchmark import Timer, Language 

setup_py = """
import torch
a = torch.rand(10000)
"""

setup_cpp = """
auto a = torch.rand({10000});
"""

code = """
a.add(1)
"""

t = Timer(setup=setup_py, stmt=code, language=Language.PYTHON)
print(t.timeit(1000))

t = Timer(setup=setup_cpp, stmt=code, language=Language.CPP)
print(t.timeit(1000))
