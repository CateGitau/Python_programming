"""
Suppose that you are building a Customer Relationship Management (CRM) system,
and you want to display a user record in the following format: 'John Smith (California)'. 
However, if you don't have a location in your system, you want just to see "John Smith."

Create a format_customer function that takes two required positional arguments, 
first_name and last_name, and one optional keyword argument, location. 
It should return a string in the required format.
"""

def format_customer(first_name, last_name, location = None):
    full_name = '{} {}'.format(first_name, last_name)
    if location:
        return '{}({})'.format(full_name, location)
    else:
        return full_name

print(format_customer)