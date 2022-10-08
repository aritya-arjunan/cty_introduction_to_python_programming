#Recipient name
RecipientName = input('Recipient name:')
#Address
Address = input('Address:')
#CardText inside postcard
CardText = input('Text in postcard:')
#Your name
GiverName = input('Your name:')
#city or state
CityState = input('City and state:')
#Date
Date = input('Date:')
#WhiteSpace
whiteSpace = ' ' * 50
#Making the postcard
print('Deliver to:')
print('%s%s' %(whiteSpace, Address))
print('%s%s' %(whiteSpace, CityState))
print('Deliver on: %s' % Date)
print('''Dear %s

%s

Sincerely,
%s''' % (RecipientName, CardText, GiverName))
