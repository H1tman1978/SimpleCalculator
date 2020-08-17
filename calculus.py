from sympy.interactive import printing
from sympy import *
import sympy as sp

# initialize printing
printing.init_printing(use_latex=True)

# define function for differential
x = sp.Symbol('x')
f = sp.Function('f')(x)

diffeq = Eq(f.diff(x,x)-5*f, 0)
