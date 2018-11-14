# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if (re.search(r"z\w{3}z", line)):
        print(line)

# r'z...z'
# r'z.{3}z'
# r'z[a-zA-Z]{3}z
