"""
A helper function performs part of the computation of another function. 
It allows us to reuse common code without repeating ourselves. 
For example, suppose we had a few lines of code that printed out 
the elapsed time at various points in a function:
"""

def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += amount_in_aud * 0.78
    total += amount_in_gbp * 1.29
    return total

print(compute_usd_total(amount_in_gbp=10))

#Create a currency conversion function with an optional margin:

def convert_currency(amount, rate, margin=0):
     return amount * rate * (1 + margin)

#Modify the original function to use the helper function:
def compute_usd_total2(amount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += convert_currency(amount_in_aud, 0.78)
    total += convert_currency(amount_in_gbp, 1.29)
    return total

print(compute_usd_total(amount_in_gbp=10))



