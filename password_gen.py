#!/usr/bin/env python3
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
NUMBER = string.digits
symbols = ".-/*=_+"

mix = lower + upper + NUMBER + symbols
length = 16
passw = "".join(random.sample(mix,length))
print("The Password generated is :", passw)
