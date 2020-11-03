# PingAnRealty
Turn 
{ 'hired': { 'be': { 'to': { 'deserve': 'I' } } } } 
To 
{'I': {'deserve': {'to': {'be': 'hired'}}}}

Step 1 import coverage library
$ pip install coverage

Step2 run code
$ coverage run reversetest.py
{'I': {'deserve': {'to': {'be': 'hired'}}}}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Step3 See coverage
$ coverage report reversetest.py
Name             Stmts   Miss  Cover
------------------------------------
reversetest.py      28      0   100%
