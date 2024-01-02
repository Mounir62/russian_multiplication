def russian_peasant_multiplication(a, b):
    if a % 2 == 0:
        return russian_peasant_mul﻿tiplication(a//2, 2*b)
    elif a == 1:
        return b
    else:
        return russian_peasant_mul﻿tiplication(a//2, 2*b) + b
