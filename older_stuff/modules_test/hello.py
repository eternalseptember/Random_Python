# naming the files in __all__ in the __init__.py file
# OR having a blank __init__.py file
# the following works

from somefunctions.testfunct1 import *
from somefunctions.fibo import *

testfunct1("blue cheese")
fib(1000)



# naming the files in __all__ in the __init__.py file
# the following works
'''
from somefunctions import *

testfunct1.testfunct1("parmesan")
fibo.fib(100)
'''

'''
# with a blank __init__.py file, the following works
from somefunctions import testfunct1
from somefunctions import fibo

testfunct1.testfunct1("cheese")
fibo.fib(1000)
'''