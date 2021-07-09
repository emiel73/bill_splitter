import random


def lucky():
    while True:
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()
        if answer in ['yes', 'no']:
            if answer == 'no':
                return False
            else:
                return True
        else:
            print('Wrong answer!')


def count_bill():
    while True:
        try:
            user_input = int(input('Enter the total bill value:\n'))
            if user_input <= 0:
                raise ValueError
            return user_input
        except ValueError:
            print('Enter valid value!')


random.seed()

try:
    number_of_guests = int(input("Enter the number of friends joining (including you):\n"))
    if number_of_guests <= 0:
        raise ValueError
except ValueError:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
guests_dict = {input(): 0 for _ in range(number_of_guests)}
total_bill = count_bill()

if lucky():
    lucky_one = random.choice(list(guests_dict.keys()))
    print(f'{lucky_one} is the lucky one!\n')
    guests_dict = {guest: round(total_bill / (number_of_guests - 1), 2) for guest in guests_dict}
    guests_dict[lucky_one] = 0
    print(guests_dict)
else:
    print('No one is going to be lucky\n')
    guests_dict = {guest: round(total_bill / number_of_guests, 2) for guest in guests_dict}
    print(guests_dict)
