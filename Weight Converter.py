weight = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')

if unit.upper() == 'L':
    converter = weight * .45
    print(f"You are {converter} lbs.")
else:
    converter = weight / .45
    print(f"You are {converter} kgs.")