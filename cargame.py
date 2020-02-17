print("Type 'help' to get started.")
str=input(">")

print('''start - to start the car.
stop - to stop the car:
quit - to exit.''')

while True:
    str=input(">").lower()

    if str == 'start':
        print("Car started. Ready to go!")
    elif str == 'stop':
        print("The car has been stopped.")
    elif str == 'quit':
        break
    else:
        print("Invalid input.")

