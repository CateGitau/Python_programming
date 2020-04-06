#Real Estate Offer

"""
The goal of this exercise is to prompt the user to bid on a house and let 
them know if and when the bid has been accepted.
"""

print('A one bedroom in the Bay Area is listed at $599,000')
print('Enter your first offer on the house.')
offer = abs(int(input()))

print('Enter your best offer on the house.')
best = abs(int(input()))

print('How much more do you want to offer each time?')
increment = abs(int(input()))

offer_accepted = False

while offer <= best:
    if offer >= 650000:
        offer_accepted = True
        print('Your offer of', offer, 'has been accepted!')
        break
    print('We\'re sorry, you\'re offer of', offer, 'has not been accepted.' )
    offer += increment