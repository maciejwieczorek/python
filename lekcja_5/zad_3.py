# !/usr/bin/env python
# encoding: utf -8

import re
regax_liczba = re.compile(
    r'''(?P<liczba> (([0-1][0-9][0-9])) | (2[0-4][0-9]) | (25(0-5)))
    )''',
    re.IGNORECASE | re.VERBOSE
)

text