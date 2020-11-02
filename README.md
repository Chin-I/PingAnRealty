# PingAnRealty
Turn 
{ 'hired': { 'be': { 'to': { 'deserve': 'I' } } } } 
To 
{'I': {'deserve': {'to': {'be': 'hired'}}}}

Step 1 import coverage library
$ pip install coverage

Step 2 run the unittest 
$ coverage run utest2.py
{'I': {'deserve': {'to': {'be': 'hired'}}}}
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK

Step 3 run the coverage %
$ coverage report utest2.py
Name        Stmts   Miss  Cover
-------------------------------
utest2.py       7      0   100%
