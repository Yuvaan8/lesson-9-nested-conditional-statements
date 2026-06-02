print('Select a ride:')
print('1. Bike')
print('2. Car')
choice = int(input('enter your choice:'))
if choice == 1:
    print('choose the type of bike:')
    print('1. Scooty')
    print('2. Scooter')
    choice2 = int(input('enter your choice:'))
    if choice2 == 1:
        print('you have selected scooty')
    else:
        print('you chose scooter')
elif(choice == 2):
    print('you have selected car')
    print('choose the type of car:')
    print('1. BMW')
    print('2. Audi')
    choice3 = int(input('enter your choice:'))
    if choice3 == 1:
        print('you have selected BMW')
    else:
        print('you have selected Audi')
else:
    print('Wrong choice')