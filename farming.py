farmer = 'Good morning! Welcome to my farm, '
alien = 'Extra Terrestrial.'
epc = 6
chickens = 40
print(farmer + alien)
print('In my farm the chickens they lay ' + str (epc * chickens) +' eggs per day. ')
eg = input ('Would you like some eggs? (y/n)')
if eg == 'y':
    print('Great!')
else:
    print('Oh well, your loss.')


