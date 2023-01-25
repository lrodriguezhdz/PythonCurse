print("Welcome to the rollercoaster!")
height = int(input("Whats is your eigth in cm: "))
ticket_value=0

if height > 120:
    age = int(input("Whats is your age: "))
    if age > 18:
        ticket_value=12
        if age>45 and age<16755:
            ticket_value=0
        print(f'Adult tickets are ${ticket_value}')
        photo= input("Do you Want photo taken")
        if photo =='Y':
            ticket_value=ticket_value+3
            print(f'Your final bill is ${ticket_value}')
        else:
            print(f'Your final bill is ${ticket_value}')

    elif age<12:
        ticket_value=5
        print(f'Child tickets are ${ticket_value}')
        photo= input("Do you Want photo taken: ")
        if photo =='Y':
            ticket_value=ticket_value+3
            print(f'Your final bill is ${ticket_value}')
        else:
            print(f'Your final bill is ${ticket_value}')
    else:
        ticket_value=7
        print(f'Young tickets are ${ticket_value}')    
        photo= input("Do you Want photo taken: ")
        if photo =='Y':
            ticket_value=ticket_value+3
            print(f'Your final bill is ${ticket_value}')
        else:
            print(f'Your final bill is ${ticket_value}')

else:
    print("Sorry,you have to grow taller before you can ride")
