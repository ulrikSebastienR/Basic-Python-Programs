weight = int(input("Enter weight: "))
unit = input("Enter unit: (K for Kilos and P for Pounds) ")

if unit.upper() == 'K':
    ans = weight*2.2
    print(f"You are {ans} lbs.")

if unit.upper() == 'P':
    ans = weight/2.2
    print(f"You are {ans} kgs.")

