"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"
"""

address = "1.1.1.1"


def defang(address):
    strin = ''
    for char in address:
        if char != ".":
            strin += char
        else:
            strin += "[.]"

    return strin

print(defang(address))
