#Check whether or not a person is eligible to join the 18-30 club

name = input('Hello, please enter your name: ')
print("Hello {}".format(name))
age = int(input('Please enter your age: '))
if 18 <= age < 31:
    print('Welcome to the 18-30 club, {}'.format(name))
else:
    print('Sorry, you aren\'t eligible for this holiday {}'.format(name))
