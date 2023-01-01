#!/usr/bin/env python3

import secrets

length = 16
passw = secrets.token_urlsafe(length)
print("Your password is: ", passw)
