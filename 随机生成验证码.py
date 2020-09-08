# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
checkcode = ''
for i in range (4):
    current = random.randrange(0,4)
    if current == i:
        tep = chr(random.randint(65,97))
    else:
        tep = random.randint(0,9)
    checkcode += str(tep)
print(checkcode)
